from pydantic import BaseModel
from typing import List

class AnswerCreate(BaseModel):
    text: str
    is_correct: bool

    class Config:
        from_attributes = True

class AnswerOut(BaseModel):
    id: int
    text: str
    is_correct: bool
    question_id: int

    class Config:
        from_attributes = True