from datetime import date
from pydantic import BaseModel, Field
import uuid

class CreditCardBase(BaseModel):
    user_id: uuid.UUID
    card_name: str
    card_holder: str
    ending_number: str | None = None  # Optional field
    bank_provider: str | None = None  # Optional field


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

class UserCreate(BaseModel):
    id: uuid.UUID
    email: str
    class Config:
        from_attributes = True

