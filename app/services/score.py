# from typing import List
# from sqlalchemy.orm import Session
# from app.models import User, Trivia, Answer
# from app.schemas import TriviaAnswer

# def calculate_score(user_answers: List[TriviaAnswer]) -> int:
#     # Calcular puntaje basado en las respuestas
#     score = 0
#     for answer in user_answers:
#         if answer.is_correct:
#             score += 10  # Suponiendo que cada respuesta correcta vale 10 puntos
#     return score
