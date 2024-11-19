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
**Crear Preguntas** `POST /questions`  
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
**Obtener lista de preguntas** `GET /questions`  
**Descripción:** Obtiene todos las preguntas registrados.
 
**Response:**
   ```json
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

### 5. Trivia
**Crear Trivia** `POST /trivias`  
**Descripción:** Crea un nueva Trivia.
 
**Body**
   ```bash
   {
    "name": "Trivia 1",
    "description": "Description 1",
    "user_ids": [
        1 
        // 1, 2, 3
    ],
    "question_ids": [
        1
        // 1, 2, 3
    ]
   }
   ```

**Response:**
   ```json
   {
    "id": 1,
    "name": "Trivia 1",
    "description": "Description 1",
    "questions": [
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
    ],
    "users": [
        {
            "id": 1,
            "name": "carloswrc3",
            "email": "carloswrc3@gmail.com"
        }
    ]
   } 
   ```
 
### 6. Obtener Trivia
**Obtener lista de Trivias** `GET /trivias`  
**Descripción:** Obtiene todos las trivias registradas.
 
**Response:**
   ```json
   [
    {
        "id": 1,
        "name": "Trivia 1",
        "description": "Description 1",
        "questions": [
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
        ],
        "users": [
            {
                "id": 1,
                "name": "carloswrc3",
                "email": "carloswrc3@gmail.com"
            }
        ]
    }
   ]
   ```

### 7. Obtener Trivia por Usuario
**Obtener lista de trivias por usuario** `GET /trivias/user/{id_user}`  
**Descripción:** Obtiene todas las trivias asociadas a un usuario.
 
**Response:**
   ```json
   [
    {
        "id": 1,
        "name": "Trivia 1",
        "description": "Description 1",
        "questions": [
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
    }
   ]
   ```

### 8. Participacion
**Crear Trivia** `POST /participations`  
**Descripción:** Cuando un usuario comienza la trivia, se genera un registro para rastrear su estado. Después de este registro, el usuario podrá comenzar a responder las preguntas.
 
**Body**
   ```bash
   {
    "trivia_id":1,
    "user_id":1
   }
   ```

**Response:**
   ```json
   {
    "id": 1,
    "trivia_id": 1,
    "user_id": 1,
    "score": 0,
    "completed": false
   }
   ```
 
### 9. Obtener Participaciones
**Obtener lista de Participaciones** `GET /participations`  
**Descripción:** Obtiene todas las participaciones registradas.
 
**Response:**
   ```json
   [
    {
        "id": 1,
        "trivia_id": 1,
        "user_id": 1,
        "score": 0,
        "completed": false
    }
   ]
   ```

### 10. Responder Trivia
**Crear Trivia** `POST /participations/{id_participation}/answer`  
**Descripción:** Anteriormente se proporcionaban las preguntas y respuestas, pero ahora solo debemos enviar los valores necesarios para participar en la trivia (usuario, preguntas y respuestas) y luego nos devuelve nuestro puntaje.
 
**Body**
   ```bash
   {
    "user_id": 1,
    "answers": [
        {
        "question_id": 1,
        "answer_id": 2
        },
        {
        "question_id": 2,
        "answer_id": 4
        }
        ,
        {
        "question_id": 3,
        "answer_id": 9
        }
    ]
   }

   ```

**Response:**
   ```json
   {
    "message": "Answers submitted",
    "score": 0
   }
   ```

### 11. Obtener Ranking
**Obtener lista de rankings por trivia** `GET /ranking/{id_trivia}/ranking`  
**Descripción:** Rankings de usuarios por trivia
 
**Response:**
   ```json
   {
    "trivia_id": 1,
    "trivia_name": "Trivia 1",
    "rankings": [
        {
            "user_id": 1,
            "user_name": "carloswrc3",
            "score": 0
        }
    ]
   }
   ```   