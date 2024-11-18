from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class TriviaParticipationAnswer(Base):
    __tablename__ = "trivia_participation_answers"

    id = Column(Integer, primary_key=True, index=True)
    participation_id = Column(Integer, ForeignKey("trivia_participation.id"), nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    is_correct = Column(Boolean, nullable=False)
