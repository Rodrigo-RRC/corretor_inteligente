# app/main.py

from fastapi import FastAPI
from app.routes.perguntas import router as pergunta_router

app = FastAPI()

app.include_router(pergunta_router, prefix="")
