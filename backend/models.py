from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# Athlete table
class Athlete(Base):
    __tablename__ = "athletes"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    age = Column(Integer)
    sport = Column(String)

    feedback = relationship("Feedback", back_populates="athlete")

# Workshop table
class Workshop(Base):
    __tablename__ = "workshops"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    date = Column(String)

# Skill table
class Skill(Base):
    __tablename__ = "skills"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    athlete_id = Column(Integer, ForeignKey("athletes.id"))

# Feedback table
class Feedback(Base):
    __tablename__ = "feedback"
    
    id = Column(Integer, primary_key=True, index=True)
    athlete_id = Column(Integer, ForeignKey("athletes.id"))
    comments = Column(Text)
    rating = Column(Float)

    athlete = relationship("Athlete", back_populates="feedback")
 
