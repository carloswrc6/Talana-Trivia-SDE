from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from app.database import engine, Base
from app.routes import users, trivias, questions, trivia_participation, ranking

# Importar todos los modelos para registrar relaciones en SQLAlchemy
from app.models import user, trivia, answer, question

# Configuración de la aplicación FastAPI
app = FastAPI(
    title="TalaTrivia API",
    description="API para gestionar usuarios, trivias y preguntas en el juego TalaTrivia.",
    version="1.0.0"
)

# Middleware para habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia esto a dominios específicos en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Manejo global de errores de validación
# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     return JSONResponse(
#         status_code=422,
#         content={"detail": exc.errors(), "body": exc.body},
#     )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    errors = exc.errors()
    formatted_errors = [
        {"loc": error["loc"], "msg": error["msg"], "type": error["type"]}
        for error in errors
    ]
    return JSONResponse(
        status_code=422,
        content={"detail": formatted_errors},
    )

# Endpoint de verificación de estado
@app.get("/", tags=["Health Check"])
def health_check():
    return {"status": "ok", "message": "TalaTrivia API is running"}

# Registrar las rutas de los diferentes módulos
app.include_router(users.router)
app.include_router(questions.router)
app.include_router(trivias.router)
app.include_router(trivia_participation.router)
app.include_router(ranking.router)