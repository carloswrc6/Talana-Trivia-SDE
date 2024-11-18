from pydantic import BaseModel

class ScoreCreate(BaseModel):
    participant_id: int
    points: int

class ScoreOut(BaseModel):
    id: int
    participant_id: int
    points: int

    class Config:
        from_attributes = True
