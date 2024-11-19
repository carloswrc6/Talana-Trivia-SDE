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
    # Verificar si la trivia existe
    trivia = db.query(Trivia).filter(Trivia.id == participation.trivia_id).first()
    if not trivia:
        raise HTTPException(status_code=404, detail="Trivia not found")
    
    # Verificar si el usuario existe
    user = db.query(User).filter(User.id == participation.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Verificar si el usuario ya está participando en la trivia
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
    # Verificar si la participación existe
    participation = db.query(TriviaParticipation).filter(TriviaParticipation.id == participation_id).first()
    if not participation:
        raise HTTPException(status_code=404, detail="Participation not found")
    
    # Verificar si el usuario que envía la respuesta es el mismo de la participación
    if participation.user_id != participation_answer.user_id:
        raise HTTPException(status_code=403, detail="User not authorized for this participation")
    
    # Verificar si la trivia ya está completada
    if participation.completed:
        raise HTTPException(status_code=400, detail="Trivia already completed")

    # Obtener las preguntas asociadas a la trivia
    trivia_questions = {q.id for q in participation.trivia.questions}

    total_score = 0

    for answer in participation_answer.answers:
        # Verificar si la pregunta existe
        question = db.query(Question).filter(Question.id == answer.question_id).first()
        if not question:
            raise HTTPException(status_code=404, detail=f"Question {answer.question_id} not found")
        
        # Verificar si la pregunta pertenece a la trivia
        if answer.question_id not in trivia_questions:
            raise HTTPException(
                status_code=400, 
                detail=f"Question {answer.question_id} does not belong to this trivia"
            )
        
        # Validar si la respuesta es una opción válida de la pregunta
        selected_answer = next((opt for opt in question.answers if opt.id == answer.answer_id), None)

        if not selected_answer:
            raise HTTPException(
                status_code=400, 
                detail=f"Invalid answer {answer.answer_id} for question {answer.question_id}"
            )
        
        # Verificar si la respuesta seleccionada es correcta
        is_correct = selected_answer.is_correct
        total_score += question.points if is_correct else 0

        # Registrar la respuesta del usuario
        participation_answer = TriviaParticipationAnswer(
            participation_id=participation_id,
            question_id=answer.question_id,
            is_correct=is_correct
        )
        db.add(participation_answer)

    # Actualizar el puntaje de la participación y marcarla como completada
    participation.score = total_score
    participation.completed = True
    db.commit()

    return {"message": "Answers submitted", "score": total_score}

@router.get("/", response_model=List[TriviaParticipationOut])
def get_all_participations(db: Session = Depends(get_db)):
    # Obtener todas las participaciones
    participations = db.query(TriviaParticipation).all()

    # Si no se encontraron participaciones, lanzamos una excepción
    if not participations:
        raise HTTPException(status_code=404, detail="No participations found")

    return participations