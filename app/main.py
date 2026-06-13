from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from app.database import engine
from app import models
from app.routers import tasks

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager")

templates = Jinja2Templates(directory="app/templates")

app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "Task Manager API is running!"}