from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.trivia import TriviaCreate, TriviaOut
from sqlalchemy.exc import IntegrityError
from app.models import Trivia, User, Participant, Question

router = APIRouter(prefix="/trivias", tags=["Trivias"])

@router.post("/", response_model=TriviaOut)
async def create_trivia(
    trivia: TriviaCreate, db: Session = Depends(get_db)
):
    # Verificar si los usuarios y preguntas existen en la base de datos
    creator = db.query(User).filter(User.id == trivia.creator_id).first()
    if not creator:
        raise HTTPException(status_code=404, detail="Creator not found")
    
    participants = db.query(User).filter(User.id.in_(trivia.participant_ids)).all()
    if len(participants) != len(trivia.participant_ids):
        raise HTTPException(status_code=404, detail="Some participants not found")

    questions = db.query(Question).filter(Question.id.in_(trivia.question_ids)).all()
    if len(questions) != len(trivia.question_ids):
        raise HTTPException(status_code=404, detail="Some questions not found")

    # Crear la trivia
    new_trivia = Trivia(
        title=trivia.title,
        description=trivia.description,
        creator_id=trivia.creator_id  # Asignar el creador
    )

    # Agregar los participantes y las preguntas a la trivia
    new_trivia.participants = participants
    new_trivia.questions = questions

    db.add(new_trivia)
    db.commit()
    db.refresh(new_trivia)

    return TriviaOut(
        id=new_trivia.id,
        title=new_trivia.title,
        description=new_trivia.description,
        creator_id=new_trivia.creator_id,
        participants=[user.id for user in new_trivia.participants],
        questions=[question.id for question in new_trivia.questions]
    )