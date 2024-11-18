from app.models.question import Difficulty
from pydantic import BaseModel, validator
from typing import List
from app.schemas.answer import AnswerOut, AnswerCreate
from fastapi import HTTPException

class QuestionCreate(BaseModel):
    text: str
    difficulty: Difficulty = Difficulty.EASY
    answers: List[AnswerCreate]  # List of answers

    # @validator("answers")
    # def validate_answers(cls, answers):
    #     if not answers or len(answers) < 1:
    #         raise ValueError("Debe incluir al menos una respuesta.")
    #     correct_answers = [answer for answer in answers if answer.is_correct]
    #     if len(correct_answers) != 1:
    #         raise ValueError("Debe haber exactamente una respuesta correcta.")
    #     return answers

    @validator("answers")
    def validate_answers(cls, answers):
        if not answers or len(answers) < 1:
            raise HTTPException(status_code=422, detail="Debe incluir al menos una respuesta.")
        correct_answers = [answer for answer in answers if answer.is_correct]
        if len(correct_answers) != 1:
            raise HTTPException(status_code=422, detail="Debe haber exactamente una respuesta correcta.")
        return answers
    
    class Config:
        from_attributes = True

class QuestionOut(BaseModel):
    id: int
    text: str
    difficulty: Difficulty  # Nivel de dificultad
    points: int  # Puntos asignados
    answers: List[AnswerOut]  # Lista de respuestas asociadas

    class Config:
        from_attributes = True        