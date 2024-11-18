from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
from app.models.trivia_user import trivia_users  # Importar la tabla intermedia

class Trivia(Base):
    __tablename__ = "trivias"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), unique=True, index=True, nullable=False)
    description = Column(String(500), nullable=True)
    creator_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relación con preguntas
    questions = relationship('Question', back_populates='trivia')
    # Relación con usuarios (relación many-to-many)
    users = relationship('User', secondary=trivia_users, back_populates='trivias')
    participants = relationship('Participant', back_populates='trivia')
