from fastapi import FastAPI
from .database import engine
from .routers import register, redirect
from . import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(register.router)
app.include_router(redirect.router)