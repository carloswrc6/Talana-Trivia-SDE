# routes/trivia.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas
from app.models.trivia import Trivia
from app.models.user import User
from app.models.question import Question
from app.schemas.trivia import TriviaOut, TriviaCreate, TriviaUserOut

router = APIRouter(prefix="/trivias", tags=["Trivias"])

@router.post("/", response_model=TriviaOut)
def create_trivia(trivia: TriviaCreate, db: Session = Depends(get_db)):
    # Validar que las listas de user_ids y question_ids no estén vacías
    if not trivia.user_ids:
        raise HTTPException(status_code=400, detail="Debe haber al menos un usuario asociado.")
    if not trivia.question_ids:
        raise HTTPException(status_code=400, detail="Debe haber al menos una pregunta asociada.")

    # Obtener las preguntas y usuarios de la base de datos
    questions = db.query(Question).filter(Question.id.in_(trivia.question_ids)).all()
    users = db.query(User).filter(User.id.in_(trivia.user_ids)).all()

    # Verificar que las preguntas solicitadas existan
    if len(questions) != len(trivia.question_ids):
        raise HTTPException(status_code=404, detail="Algunas preguntas no se encuentran.")

    # Verificar que los usuarios solicitados existan
    if len(users) != len(trivia.user_ids):
        raise HTTPException(status_code=404, detail="Algunos usuarios no se encuentran.")

    # Crear la trivia
    db_trivia = Trivia(
        name=trivia.name,
        description=trivia.description,
    )

    # Asociar las preguntas a la trivia
    db_trivia.questions = questions
    # No es necesario asociar usuarios si no quieres que aparezcan en la respuesta
    db_trivia.users = users

    db.add(db_trivia)
    db.commit()
    db.refresh(db_trivia)

    return db_trivia

@router.get("/", response_model=List[TriviaOut])
def get_trivias(db: Session = Depends(get_db)):
    return db.query(Trivia).all()

@router.get("/user/{user_id}", response_model=List[TriviaUserOut])
def get_trivias_for_user(user_id: int, db: Session = Depends(get_db)):
    
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    trivias = db.query(Trivia).join(Trivia.users).filter(User.id == user_id).all()
    if not trivias:
        raise HTTPException(status_code=404, detail="No trivias found for this user")
    return trivias