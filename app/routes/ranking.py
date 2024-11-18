
# routes/trivia.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas
from app.models.trivia import Trivia
from app.models.user import User
from app.models.trivia_participation import TriviaParticipation
from app.models.question import Question
from app.schemas.ranking import TriviaRanking, UserRanking

router = APIRouter(prefix="/ranking", tags=["Trivias"])

@router.get("/{trivia_id}/ranking", response_model=TriviaRanking)
def get_trivia_ranking(trivia_id: int, db: Session = Depends(get_db)):
    # Verificar si la trivia existe
    trivia = db.query(Trivia).filter(Trivia.id == trivia_id).first()
    if not trivia:
        raise HTTPException(status_code=404, detail="Trivia not found")

    # Obtener las participaciones y calcular el ranking
    participations = (
        db.query(TriviaParticipation, User)
        .join(User, TriviaParticipation.user_id == User.id)
        .filter(TriviaParticipation.trivia_id == trivia_id)
        .order_by(TriviaParticipation.score.desc())
        .all()
    )

    # Formatear el ranking
    rankings = [
        UserRanking(
            user_id=participation.user_id,
            user_name=user.name,
            score=participation.score,
        )
        for participation, user in participations
    ]

    return TriviaRanking(
        trivia_id=trivia.id,
        trivia_name=trivia.name,
        rankings=rankings,
    )
