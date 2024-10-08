from sqlalchemy import create_engine, Column, Integer, String, Float, Date, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.sql import func

DATABASE_URL = "sqlite:///./credit_card_tracker.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    credit_cards = relationship("CreditCard", back_populates="user")  # Add this line

class CreditCard(Base):
    __tablename__ = "credit_cards"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    card_name = Column(String)
    card_holder = Column(String)
    ending_number = Column(String)  # Last 4 digits
    bank_provider = Column(String)
    welcome_bonus = Column(String)
    welcome_spending_amount = Column(Float)
    welcome_spending_deadline = Column(Date)
    notes = Column(String, nullable=True)
    open_date = Column(Date, nullable=True)
    approved_date = Column(Date, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    user = relationship("User", back_populates="credit_cards")
    bonuses = relationship("Bonus", back_populates="credit_card")

class Bonus(Base):
    __tablename__ = "bonuses"
    id = Column(Integer, primary_key=True, index=True)
    credit_card_id = Column(Integer, ForeignKey("credit_cards.id"))
    bonus_type = Column(String)  # e.g., "yearly spending", "quarterly spending"
    points = Column(Integer)
    amount_spending_required = Column(Float)
    deadline = Column(Date)
    created_at = Column(DateTime, server_default=func.now())
    credit_card = relationship("CreditCard", back_populates="bonuses")

Base.metadata.create_all(bind=engine)