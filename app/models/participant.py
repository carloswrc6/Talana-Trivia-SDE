from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base

class Participant(Base):
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # Usuario participante
    trivia_id = Column(Integer, ForeignKey("trivias.id"), nullable=False)  # Trivia en la que participa
    total_score = Column(Integer, default=0)  # Puntaje total acumulado
    joined_at = Column(DateTime, server_default=func.now())  # Fecha de participación

    # Relaciones
    user = relationship("User", back_populates="participations")
    trivia = relationship('Trivia', back_populates='participants')
    scores = relationship("Score", back_populates="participant", cascade="all, delete-orphan")