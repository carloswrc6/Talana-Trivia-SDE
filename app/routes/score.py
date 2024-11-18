from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.score import Score
from app.schemas.score import ScoreCreate, ScoreOut

router = APIRouter(prefix="/scores", tags=["Scores"])

@router.post("/", response_model=ScoreOut)
def create_score(score: ScoreCreate, db: Session = Depends(get_db)):
    db_score = Score(participant_id=score.participant_id, points=score.points)
    db.add(db_score)
    db.commit()
    db.refresh(db_score)
    return db_score

@router.get("/", response_model=List[ScoreOut])
def list_scores(db: Session = Depends(get_db)):
    return db.query(Score).all()
