# TalaTrivia API

## Introducción
Bienvenido a **TalaTrivia**, una API diseñada para gestionar un emocionante juego de trivia enfocado en recursos humanos. Esta API permite:
- Gestionar usuarios
- Crear y listar preguntas
- Crear trivias con diferentes niveles de dificultad
- Registrar la participación de usuarios en las trivias
- Generar un ranking basado en los puntajes de los jugadores

## Requisitos
- **Python 3.12+**
- **Docker** (opcional, pero recomendado)
- **PostgreSQL** como base de datos

## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/carloswrc6/Talana-Trivia-SDE.git
   cd talatrivia

2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt

3. Configura las variables de entorno necesarias en un archivo .env:
   ```bash
   DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/talatrivia
   POSTGRES_USER=user
   POSTGRES_PASSWORD=password
   POSTGRES_DB=talatrivia

4. Levanta el servidor de desarrollo:
   ```bash
   docker-compose up --build

5. Accede a la documentación interactiva:
   Swagger UI: http://localhost:8000/docs
   ReDoc: http://localhost:8000/redoc   


## Endpoints Disponibles

### 1. Usuarios
**Crear Usuario** `POST /users`  
**Descripción:** Crea un nuevo usuario.

**Body:**
   ```json
   {
   "name": "John Doe",
   "email": "john.doe@example.com"
   }

Response:
   ```json
   {
   "id": 1,
   "name": "John Doe",
   "email": "john.doe@example.com"
   }