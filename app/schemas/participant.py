from pydantic import BaseModel

class ParticipantCreate(BaseModel):
    user_id: int
    trivia_id: int

class ParticipantOut(BaseModel):
    id: int
    user_id: int
    trivia_id: int

    class Config:
        from_attributes = True
