from decouple import config  # Usar python-decouple
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "postgresql://user:password@db:5432/talatrivia"
DATABASE_URL = config("DATABASE_URL", default="postgresql://user:password@localhost/talatrivia")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base: DeclarativeMeta = declarative_base()

# Dependency para inyectar la sesión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
