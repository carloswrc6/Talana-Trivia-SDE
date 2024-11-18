from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas
from app.schemas.question import QuestionCreate

router = APIRouter(prefix="/questions", tags=["Questions"])

# routes/questions.py
@router.post("/")
async def create_question(
    question: QuestionCreate, db: Session = Depends(get_db)
):
    db_question = crud.create_question(db=db, question=question)
    return db_question

@router.get("/", response_model=List[schemas.QuestionOut])
def get_questions(db: Session = Depends(get_db)):
    return crud.get_questions(db=db)
