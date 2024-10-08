from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException, status, Request, Header
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session


from . import models, schemas
from .dependencies import get_db, get_current_user, supabase

import logging

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
app = FastAPI()


@app.post("/auth/signup")
async def signup(data: schemas.UserCreate):
    try:
        # Remove the await keyword here
        print(data.model_dump())
        user = supabase.auth.sign_up(data.model_dump())
        # Check for errors in the data attribute
        if not user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=user.data.error.message
            )
        return {"message": "User created successfully", "user": user}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@app.post("/auth/login")
async def login(data: schemas.UserCreate):  # Expect data in request body
    try:
        user = supabase.auth.sign_in_with_password(data.model_dump())
        if not user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User login failed")
        return {"message": "User login successfully", "user": user}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@app.post("/auth/google/login")
async def google_login():
    """Initiates the Google login flow."""
    try:
        # Get the URL for redirecting the user to Google for authentication.
        # This URL will handle the OAuth flow and redirect the user back to your app.
        redirect_url = "https://swepuhgtuviijqvdptmp.supabase.co/auth/v1/callback"  # Replace with your actual redirect URL
        auth_response = supabase.auth.sign_in_with_oauth(
            {"provider": "google", "options": {"redirectTo": redirect_url}}
        )
        return {"url": auth_response.url}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@app.post("/credit_cards/", response_model=schemas.CreditCard)
async def create_credit_card(
    credit_card: schemas.CreditCardCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)  # Protect the endpoint
):
     # Access the user's ID from the Supabase user object
    user_id = current_user.id

    # Create the CreditCard object with the user_id
    db_credit_card = models.CreditCard(
        user_id=credit_card.user_id,
        card_name=credit_card.card_name,
        card_holder=credit_card.card_holder,
        ending_number=credit_card.ending_number,
        bank_provider=credit_card.bank_provider,
        welcome_bonus=credit_card.welcome_bonus,
        welcome_spending_amount=credit_card.welcome_spending_amount,
        welcome_spending_deadline=credit_card.welcome_spending_deadline,
    )
    db.add(db_credit_card)
    db.commit()
    db.refresh(db_credit_card)
    return db_credit_card


@app.get("/credit_cards/", response_model=list[schemas.CreditCard])
async def read_credit_cards(db: Session = Depends(get_db)):
    credit_cards = db.query(models.CreditCard).all()
    return credit_cards


@app.get("/credit_cards/{credit_card_id}", response_model=schemas.CreditCard)
async def read_credit_card(credit_card_id: int, db: Session = Depends(get_db)):
    credit_card = (
        db.query(models.CreditCard)
        .filter(models.CreditCard.id == credit_card_id)
        .first()
    )
    if credit_card is None:
        raise HTTPException(status_code=404, detail="Credit card not found")
    return credit_card


@app.put("/credit_cards/{credit_card_id}", response_model=schemas.CreditCard)
async def update_credit_card(
    credit_card_id: int,
    request: Request,  # Use Request to access the raw request body
    db: Session = Depends(get_db),
):
    db_credit_card = (
        db.query(models.CreditCard)
        .filter(models.CreditCard.id == credit_card_id)
        .first()
    )
    if db_credit_card is None:
        raise HTTPException(status_code=404, detail="Credit card not found")

    update_data = await request.json()  # Get the raw JSON data

    # Update only the provided fields
    for key, value in update_data.items():
        if hasattr(db_credit_card, key):  # Check if the field exists in the model
            setattr(db_credit_card, key, value)

    db.commit()
    db.refresh(db_credit_card)
    return db_credit_card


@app.delete("/credit_cards/{credit_card_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_credit_card(credit_card_id: int, db: Session = Depends(get_db)):
    db_credit_card = (
        db.query(models.CreditCard)
        .filter(models.CreditCard.id == credit_card_id)
        .first()
    )
    if db_credit_card is None:
        raise HTTPException(status_code=404, detail="Credit card not found")
    db.delete(db_credit_card)
    db.commit()


@app.post("/bonuses/", response_model=schemas.Bonus)
async def create_bonus(bonus: schemas.BonusCreate, db: Session = Depends(get_db)):
    db_bonus = models.Bonus(**bonus.model_dump())
    db.add(db_bonus)
    db.commit()
    db.refresh(db_bonus)

    # Format created_at before validation
    db_bonus.created_at = db_bonus.created_at.date()

    bonus_schema = schemas.Bonus.model_validate(db_bonus)
    response_bonus = bonus_schema.model_dump(by_alias=True)
    # No need to format created_at again here

    return response_bonus


@app.get("/bonuses/", response_model=list[schemas.Bonus])
async def read_bonuses(db: Session = Depends(get_db)):
    """Retrieve all bonuses."""
    bonuses = db.query(models.Bonus).all()

    # Format dates before validation
    for bonus in bonuses:
        bonus.created_at = bonus.created_at.date()

    bonus_list = []
    for bonus in bonuses:
        bonus_data = schemas.Bonus.model_validate(
            bonus
        ).model_dump()  # Use the default serialization
        bonus_list.append(bonus_data)

    return bonus_list


@app.get("/bonuses/{bonus_id}", response_model=schemas.Bonus)
async def read_bonus(bonus_id: int, db: Session = Depends(get_db)):
    """Retrieve a specific bonus by ID."""
    bonus = db.query(models.Bonus).filter(models.Bonus.id == bonus_id).first()
    if bonus is None:
        raise HTTPException(status_code=404, detail="Bonus not found")

    # Format the date before returning
    bonus.created_at = bonus.created_at.date()

    return bonus


@app.put("/bonuses/{bonus_id}", response_model=schemas.Bonus)
async def update_bonus(
    bonus_id: int,
    request: Request,  # Use Request to access the raw request body
    db: Session = Depends(get_db),
):
    """Update a bonus."""

    db_bonus = db.query(models.Bonus).filter(models.Bonus.id == bonus_id).first()

    if db_bonus is None:
        raise HTTPException(status_code=404, detail="Bonus not found")
    update_data = await request.json()  # Get the raw JSON data

    # Update only the provided fields
    for key, value in update_data.items():
        if hasattr(db_bonus, key):  # Check if the field exists in the model
            setattr(db_bonus, key, value)

    db.commit()
    db.refresh(db_bonus)

    # Format the date before returning
    db_bonus.created_at = db_bonus.created_at.date()
    return db_bonus


@app.delete("/bonuses/{bonus_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_bonus(bonus_id: int, db: Session = Depends(get_db)):
    """Delete a bonus."""
    db_bonus = db.query(models.Bonus).filter(models.Bonus.id == bonus_id).first()
    if db_bonus is None:
        raise HTTPException(status_code=404, detail="Bonus not found")
    db.delete(db_bonus)
    db.commit()


@app.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/users/", response_model=list[schemas.User])
async def read_users(db: Session = Depends(get_db)):
    """Retrieve all users."""
    users = db.query(models.User).all()
    return users


@app.put("/users/{user_id}", response_model=schemas.User)
async def update_user(
    user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)
):
    """Update a user."""
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Update the user's email
    db_user.email = user.email

    db.commit()
    db.refresh(db_user)
    return db_user


@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Delete a user."""
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
