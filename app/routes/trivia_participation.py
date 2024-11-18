from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.trivia_participation import TriviaParticipation
from app.models.trivia import Trivia
from app.models.user import User
from app.models.trivia_participation_answer import TriviaParticipationAnswer
from app.models.question import Question
from app.schemas.trivia import Answer, TriviaParticipationCreate, TriviaParticipationOut
from typing import List
from app.schemas.trivia import ParticipationAnswer, TriviaOut

router = APIRouter(prefix="/participations", tags=["Participations"])

@router.post("/", response_model=TriviaParticipationOut)
def create_participation(participation: TriviaParticipationCreate, db: Session = Depends(get_db)):
    # Verificar si el usuario ya está participando
    existing = db.query(TriviaParticipation).filter(
        TriviaParticipation.trivia_id == participation.trivia_id,
        TriviaParticipation.user_id == participation.user_id
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Participation already exists")

    # Crear nueva participación
    new_participation = TriviaParticipation(
        trivia_id=participation.trivia_id,
        user_id=participation.user_id,
    )
    db.add(new_participation)
    db.commit()
    db.refresh(new_participation)
    return new_participation

@router.post("/{participation_id}/answer")
def submit_answers(participation_id: int, participation_answer: ParticipationAnswer, db: Session = Depends(get_db)):
    participation = db.query(TriviaParticipation).filter(TriviaParticipation.id == participation_id).first()
    if not participation:
        raise HTTPException(status_code=404, detail="Participation not found")
    if participation.user_id != participation_answer.user_id:  # Usar el user_id del body
        raise HTTPException(status_code=403, detail="User not authorized for this participation")
    if participation.completed:
        raise HTTPException(status_code=400, detail="Trivia already completed")

    # Calcular puntaje
    total_score = 0
    for answer in participation_answer.answers:
        question = db.query(Question).filter(Question.id == answer.question_id).first()
        if not question:
            raise HTTPException(status_code=404, detail=f"Question {answer.question_id} not found")
        correct_answer = next((opt for opt in question.answers if opt.is_correct), None)
        is_correct = correct_answer and correct_answer.id == answer.answer_id
        total_score += question.points if is_correct else 0

        # Registrar la respuesta
        participation_answer = TriviaParticipationAnswer(
            participation_id=participation_id,
            question_id=answer.question_id,
            is_correct=is_correct
        )
        db.add(participation_answer)

    participation.score = total_score
    participation.completed = True
    db.commit()
    return {"message": "Answers submitted", "score": total_score}


@router.get("/user/{user_id}", response_model=List[TriviaOut])
def get_trivias_for_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    participations = db.query(TriviaParticipation).filter(TriviaParticipation.user_id == user_id).all()
    trivias = [participation.trivia for participation in participations]

    return trivias
