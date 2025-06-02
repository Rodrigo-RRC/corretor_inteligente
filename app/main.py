# app/main.py

from fastapi import FastAPI
from app.services import chat  # <- caminho correto

app = FastAPI()

app.include_router(chat.router, prefix="")

