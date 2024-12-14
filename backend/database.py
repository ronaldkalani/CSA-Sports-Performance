from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Load environment variables (optional, for security)
from dotenv import load_dotenv

load_dotenv()

# PostgreSQL Database URL
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://username:password@localhost/sports_performance")

# Create the database engine
engine = create_engine(DATABASE_URL)

# Session local for handling transactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all ORM models
Base = declarative_base()

def get_db():
    """Dependency to get the database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 
