from pydantic_settings import BaseSettings  # Update the import
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()