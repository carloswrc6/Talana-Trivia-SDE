from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Score(Base):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True, index=True)
    participant_id = Column(Integer, ForeignKey("participants.id"), nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    answer_id = Column(Integer, ForeignKey("answers.id"), nullable=True)  # Este es el que causa el error
    is_correct = Column(Boolean, nullable=False)
    points_earned = Column(Integer, nullable=False)

    participant = relationship("Participant", back_populates="scores")
    question = relationship("Question", back_populates="scores")
    answer = relationship("Answer", back_populates="scores")  # Asegúrate de que la relación esté aquí

