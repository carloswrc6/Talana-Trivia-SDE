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
 
**Body**
   ```bash
   {
      "name": "John Doe",
      "email": "john.doe@example.com"
   }
   ```

**Response:**
   ```json
   {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
   }
   ```

### 2. Obtener Usuarios
**Obtener lista de usuarios** `GET /users`  
**Descripción:** Obtiene todos los usuarios registrados.

**Response:**
   ```json
   [
      {
         "id": 1,
         "name": "John Doe",
         "email": "john.doe@example.com"
      },
      {
         "id": 2,
         "name": "Jane Smith",
         "email": "jane.smith@example.com"
      }
   ]
   ```

### 3. Preguntas
**Crear Usuario** `POST /questions`  
**Descripción:** Crea un nueva pregunta.
 
**Body**
   ```bash
   {
      "text": "questions 3",
         // difficulty : easy, medium, hard
      "difficulty": "hard",
      "answers": [
         {
            "text": "answers a",
            "is_correct": true
         },
         {
            "text": "answers b",
            "is_correct": false
         },
         {
            "text": "answers c",
            "is_correct": false
         }
      ]
   }
   ```

**Response:**
   ```json
   {
      "text": "questions 3",
      "points": 2005,
      "difficulty": "hard",
      "id": 1,
      "trivia_id": null,
      "answers": [
         {
               "is_correct": true,
               "text": "answers a",
               "id": 1,
               "question_id": 1
         },
         {
               "is_correct": false,
               "text": "answers b",
               "id": 2,
               "question_id": 1
         },
         {
               "is_correct": false,
               "text": "answers c",
               "id": 3,
               "question_id": 1
         }
      ]
   }
   ```
 
 
### 4. Obtener Preguntas
**Crear Usuario** `GET /questions`  
**Descripción:** Obtiene todos las preguntas registrados.
 
**Response:**
   ```bash
   [
    {
        "id": 1,
        "text": "questions 3",
        "difficulty": "hard",
        "points": 2005,
        "answers": [
            {
                "id": 1,
                "text": "answers a",
                "is_correct": true,
                "question_id": 1
            },
            {
                "id": 2,
                "text": "answers b",
                "is_correct": false,
                "question_id": 1
            },
            {
                "id": 3,
                "text": "answers c",
                "is_correct": false,
                "question_id": 1
            }
        ]
    }
   ]
   ```
