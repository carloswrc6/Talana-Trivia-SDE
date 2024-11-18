from pydantic import BaseModel
from typing import Optional, List
from app.schemas.question import QuestionOut
from app.schemas.user import UserOut

class TriviaCreate(BaseModel):
    title: str
    description: Optional[str]
    creator_id: int  # ID del creador de la trivia
    participant_ids: List[int]  # Lista de los IDs de los usuarios participantes
    question_ids: List[int]  # Lista de IDs de preguntas

class TriviaOut(BaseModel):
    id: int
    title: str
    description: str
    creator_id: int
    participants: List[int]
    questions: List[int]

    class Config:
        from_attributes = True
