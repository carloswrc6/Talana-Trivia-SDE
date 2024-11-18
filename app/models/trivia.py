# models/trivia.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
from app.models.user import User
from app.models.question import Question
from app.models.trivia_participation import TriviaParticipation

class Trivia(Base):
    __tablename__ = "trivias"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Nombre de la trivia
    description = Column(String, nullable=True)  # Descripción de la trivia
    created_at = Column(DateTime, server_default=func.now())  # Fecha de creación
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())  # Fecha de actualización

    # Relación con preguntas
    questions = relationship("Question", back_populates="trivia")
    
    # Relación con usuarios (mediante la tabla intermedia)
    users = relationship("User", secondary="trivia_users", back_populates="trivias")

    participations = relationship(
        "TriviaParticipation", back_populates="trivia", cascade="all, delete-orphan"
    )