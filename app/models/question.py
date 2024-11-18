from sqlalchemy.orm import validates
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy import Enum
from enum import Enum as PyEnum

class Difficulty(PyEnum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

# Diccionario que asigna puntos por nivel de dificultad
DIFFICULTY_POINTS = {
    Difficulty.EASY: 505,
    Difficulty.MEDIUM: 1005,
    Difficulty.HARD: 2005,
}

class Question(Base):

    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)  # Texto de la pregunta
    difficulty = Column(Enum(Difficulty), nullable=False)  # Nivel de dificultad (easy, medium, hard)
    points = Column(Integer, nullable=False)  # Puntos asignados a la pregunta

    # Relación para las opciones de respuesta
    answers = relationship("Answer", back_populates="question", cascade="all, delete-orphan")

    # Relación con los puntajes (si se requiere)
    scores = relationship("Score", back_populates="question")
    
    # Clave foránea para la relación con Trivia
    trivia_id = Column(Integer, ForeignKey('trivias.id'))

    # Relación inversa con Trivia
    trivia = relationship('Trivia', back_populates='questions')

    def __init__(self, text: str, difficulty: Difficulty):
        """
        Inicializa una pregunta y asigna los puntos según la dificultad.
        """
        self.text = text
        self.difficulty = difficulty
        self.points = DIFFICULTY_POINTS[difficulty]

    def validate_answers(self, value: str) -> bool:
        """
        Valida si la respuesta es correcta comparándola con las respuestas predefinidas.
        Solo recibe el valor de la respuesta como parámetro.
        """
        return value in self.answers

