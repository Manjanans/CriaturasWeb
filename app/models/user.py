from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from app.core.security import verify_password, get_password_hash

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "usuarios"}
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)  # True/False for active status
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return verify_password(plain_password, hashed_password)
    
    @staticmethod
    def get_password_hash(password: str) -> str:
        return get_password_hash(password)

# Base class for other models that will be in the 'public' schema
class PublicBase(Base):
    __abstract__ = True
    __table_args__ = {"schema": "public"}

# Example of another model that would be in the public schema
class ExampleModel(PublicBase):
    __tablename__ = "example_table"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    created_at = Column(DateTime(timezone=True), server_default=func.now()) 