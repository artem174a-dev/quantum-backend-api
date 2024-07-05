from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import auth, users

app = FastAPI()

# Настройка CORS
origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Регистрация роутеров
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])