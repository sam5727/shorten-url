from fastapi import FastAPI
from routers import register, redirect

app = FastAPI()

app.include_router(register.router)
app.include_router(redirect.router)