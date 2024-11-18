# models/trivia_user.py
from sqlalchemy import Table, Column, Integer, ForeignKey
from app.database import Base

trivia_users = Table(
    "trivia_users",
    Base.metadata,
    Column("trivia_id", Integer, ForeignKey("trivias.id"), primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True)
)
