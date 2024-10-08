from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from supabase import create_client, Client
from dotenv import load_dotenv
from fastapi import Header
import os
import urllib

# Load environment variables from .env file
load_dotenv()

# Supabase connection details
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_ANON_KEY")

supabase: Client = create_client(url, key)

# Database connection string
password = os.getenv("SUPABASE_DB_PASSWORD")
# URL-encode the password to handle special characters
encoded_password = urllib.parse.quote_plus(password)
# Database connection string
DATABASE_URL = f"postgresql+psycopg2://postgres.swepuhgtuviijqvdptmp:{encoded_password}@aws-0-us-east-1.pooler.supabase.com:6543/postgres"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


from typing import Generator


def get_db() -> Generator[Session, None, None]:
    """Dependency function to provide a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta

from . import schemas, models
from .config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")  # Placeholder for OAuth2


async def get_current_user(access_token: str = Header(...)):
    try:
        # Verify the Supabase access token
        user = supabase.auth.get_user(access_token)
        # ... (optional: check if the user exists in your database)
        return user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired access token",
        )
