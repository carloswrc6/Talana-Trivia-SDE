from sqlalchemy.orm import Session
from app.models.question import Question
from app.models.user import User
from app.models.trivia import Trivia
from app.schemas.question import QuestionCreate
from app.schemas.trivia import TriviaCreate
from app.models.answer import Answer
from app.models.question import Difficulty
from sqlalchemy.orm import joinedload

def create_question(db: Session, question: QuestionCreate):
    # Crear la pregunta
    db_question = Question(
        text=question.text,
        difficulty=question.difficulty,
    )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)

    # Crear las respuestas
    for answer in question.answers:
        db_answer = Answer(
            text=answer.text,
            is_correct=answer.is_correct,
            question_id=db_question.id
        )
        db.add(db_answer)

    db.commit()
    db.refresh(db_question)

    # return db_question
    # Cargar las relaciones (como respuestas) usando joinedload
    return db.query(Question).options(joinedload(Question.answers)).filter(Question.id == db_question.id).first()


def get_questions(db: Session, difficulty: Difficulty = None):
    if difficulty:
        # Si se pasa un filtro de dificultad, se filtran las preguntas por esa dificultad
        return db.query(Question).filter(Question.difficulty == difficulty).all()
    # Si no se pasa filtro, se obtienen todas las preguntas
    return db.query(Question).all()
