# routes/trivia.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas
from app.models.trivia import Trivia
from app.models.user import User
from app.models.question import Question
from app.schemas.trivia import TriviaOut, TriviaCreate

router = APIRouter(prefix="/trivias", tags=["Trivias"])

@router.post("/", response_model=TriviaOut)
def create_trivia(trivia: TriviaCreate, db: Session = Depends(get_db)):
    # Obtener las preguntas y usuarios de la base de datos
    questions = db.query(Question).filter(Question.id.in_(trivia.question_ids)).all()
    users = db.query(User).filter(User.id.in_(trivia.user_ids)).all()

    if len(questions) != len(trivia.question_ids):
        raise HTTPException(status_code=404, detail="Algunas preguntas no se encuentran.")
    if len(users) != len(trivia.user_ids):
        raise HTTPException(status_code=404, detail="Algunos usuarios no se encuentran.")

    # Crear la trivia
    db_trivia = Trivia(
        name=trivia.name,
        description=trivia.description,
    )
    db_trivia.questions = questions
    db_trivia.users = users

    db.add(db_trivia)
    db.commit()
    db.refresh(db_trivia)

    return db_trivia

@router.get("/", response_model=List[TriviaOut])
def get_trivias(db: Session = Depends(get_db)):
    return db.query(Trivia).all()
