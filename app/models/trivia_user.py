from sqlalchemy import Column, Integer, ForeignKey, Table
from app.database import Base

# Definir la tabla intermedia entre Trivia y User
trivia_users = Table(
    'trivia_users',
    Base.metadata,
    Column('trivia_id', Integer, ForeignKey('trivias.id', ondelete='CASCADE')),
    Column('user_id', Integer, ForeignKey('users.id', ondelete='CASCADE'))
)
