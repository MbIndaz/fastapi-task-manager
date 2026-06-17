from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.database import engine
from app import models
from app.routers import tasks, auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager")
templates = Jinja2Templates(directory="app/templates")

app.include_router(tasks.router)
app.include_router(auth.router)

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse(request, "index.html", {"active": "tasks"})

@app.get("/completed", response_class=HTMLResponse)
def completed(request: Request):
    return templates.TemplateResponse(request, "completed.html", {"active": "completed"})

@app.get("/settings", response_class=HTMLResponse)
def settings(request: Request):
    return templates.TemplateResponse(request, "settings.html", {"active": "settings"})