from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import ProgrammingError
from app.core.config import settings

if not settings.DATABASE_URL:
    raise ValueError("DATABASE_URL is not set.")

# pool_pre_ping=True checks for stale connections before use
# pool_recycle=3600 recycles connections every hour
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_schemas():
    """Create the usuarios schema if it doesn't exist"""
    with engine.connect() as conn:
        try:
            conn.execute(text("CREATE SCHEMA IF NOT EXISTS usuarios;"))
            conn.commit()
        except ProgrammingError as e:
            print(f"Schema creation error (might already exist): {e}")

def get_db():
    """Dependency to get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()