from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.database import engine
from app import models
from app.routers import tasks

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager")

templates = Jinja2Templates(directory="app/templates")

app.include_router(tasks.router)

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse(request, "index.html")