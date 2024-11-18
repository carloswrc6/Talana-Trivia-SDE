from pydantic import BaseModel
from typing import List

class UserRanking(BaseModel):
    user_id: int
    user_name: str
    score: int

class TriviaRanking(BaseModel):
    trivia_id: int
    trivia_name: str
    rankings: List[UserRanking]

    class Config:
        from_attributes = True
