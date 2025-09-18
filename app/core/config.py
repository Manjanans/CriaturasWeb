import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load from .env if exists (for local dev)
load_dotenv()

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # API
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "CriaturasWeb API"
    
    class Config:
        env_file = ".env"

settings = Settings() 