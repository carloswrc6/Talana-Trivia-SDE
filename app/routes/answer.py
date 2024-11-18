from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.answer import Answer
from app.schemas.answer import AnswerOut

router = APIRouter(prefix="/answers", tags=["Answers"])

@router.post("/")
def create_answer(answer: AnswerOut, db: Session = Depends(get_db)):
    # Crear nueva respuesta para una pregunta
    new_answer = Answer(text=answer.text, is_correct=answer.is_correct, question_id=answer.question_id)
    db.add(new_answer)
    db.commit()
    db.refresh(new_answer)
    return new_answer

@router.get("/{answer_id}", response_model=AnswerOut)
def get_answer(answer_id: int, db: Session = Depends(get_db)):
    # Obtener respuesta por ID
    answer = db.query(Answer).filter(Answer.id == answer_id).first()
    if not answer:
        raise HTTPException(status_code=404, detail="Respuesta no encontrada")
    return answer