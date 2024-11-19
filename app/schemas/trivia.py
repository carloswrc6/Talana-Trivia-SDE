# schemas/trivia.py
from pydantic import BaseModel
from typing import List
from app.schemas.question import QuestionOut
from app.schemas.user import UserOut

class TriviaCreate(BaseModel):
    name: str
    description: str
    question_ids: List[int]  # IDs de las preguntas seleccionadas
    user_ids: List[int]  # IDs de los usuarios que participarán

class TriviaOut(BaseModel):
    id: int
    name: str
    description: str
    questions: List[QuestionOut]  # Preguntas asociadas
    users: List[UserOut]  # Usuarios asociados

class TriviaUserOut(BaseModel):
    id: int
    name: str
    description: str
    questions: List[QuestionOut]  # Preguntas asociadas

# Esquema para responder preguntas
class Answer(BaseModel):
    question_id: int
    answer_id: int  # ID de la respuesta seleccionada

class ParticipationAnswer(BaseModel):
    answers: List[Answer]
    user_id: int

class TriviaParticipationCreate(BaseModel):
    trivia_id: int
    user_id: int

class TriviaParticipationOut(BaseModel):
    id: int
    trivia_id: int
    user_id: int
    score: int
    completed: bool        

    class Config:
        from_attributes = True
