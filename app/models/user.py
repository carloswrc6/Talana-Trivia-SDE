from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
from app.models.trivia_user import trivia_users  # Importar la tabla intermedia
from app.models.trivia_participation import TriviaParticipation

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    email = Column(String(255), unique=True, index=True)
    # created_at = Column(DateTime, server_default=func.now())
    # updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relación con trivias
    trivias = relationship('Trivia', secondary=trivia_users, back_populates='users')
    
    participations = relationship(
        "TriviaParticipation", back_populates="user", cascade="all, delete-orphan"
    )