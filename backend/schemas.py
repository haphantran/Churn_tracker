from datetime import date
from pydantic import BaseModel, Field


class CreditCardBase(BaseModel):
    user_id: int 
    card_name: str
    card_holder: str
    ending_number: str | None = None  # Optional field
    bank_provider: str | None = None  # Optional field
    welcome_bonus: str
    welcome_spending_amount: float
    welcome_spending_deadline: date  # Use datetime.date for dates


class CreditCardCreate(CreditCardBase):
    pass  # We might add more fields here later for creation


class CreditCard(CreditCardBase):
    id: int
    notes: str | None = None
    open_date: date | None = None  # Optional fields
    approved_date: date | None = None

    class Config:
        from_attributes = (
            True  # To easily create Pydantic models from SQLAlchemy objects
        )


class BonusBase(BaseModel):
    credit_card_id: int
    bonus_type: str
    points: int
    amount_spending_required: float
    deadline: date


class BonusCreate(BonusBase):
    pass


class Bonus(BonusBase):
    id: int
    credit_card_id: int
    created_at: date

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str  # Add the password field

class User(UserBase):
    id: int

    class Config:
        from_attributes = True