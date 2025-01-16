# app/main.py
from fastapi import FastAPI
from app.routers import users
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
