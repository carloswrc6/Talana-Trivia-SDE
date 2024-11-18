# from datetime import datetime

# def validate_email(email: str, db: Session) -> bool:
#     # Verificar si el correo electrónico ya está registrado
#     existing_user = db.query(User).filter(User.email == email).first()
#     return existing_user is None

# def format_score(score: int) -> str:
#     return f"{score} puntos"

# def get_current_time():
#     return datetime.now()
