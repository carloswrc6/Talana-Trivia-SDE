from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class TriviaParticipation(Base):
    __tablename__ = "trivia_participation"

    id = Column(Integer, primary_key=True, index=True)
    trivia_id = Column(Integer, ForeignKey("trivias.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    score = Column(Integer, default=0)  # Puntaje acumulado del usuario en esta trivia
    completed = Column(Boolean, default=False)  # Indica si el usuario ha completado la trivia

    trivia = relationship("Trivia", back_populates="participations")
    user = relationship("User", back_populates="participations")
