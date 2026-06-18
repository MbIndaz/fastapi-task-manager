from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from app.database import engine, get_db
from app import models
from app.routers import tasks, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager")
templates = Jinja2Templates(directory="app/templates")

app.include_router(tasks.router)
app.include_router(auth.router)


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        return RedirectResponse(url="/login")
    return templates.TemplateResponse(request, "index.html", {"active": "tasks"})


@app.get("/completed", response_class=HTMLResponse)
def completed(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        return RedirectResponse(url="/login")
    return templates.TemplateResponse(request, "completed.html", {"active": "completed"})


@app.get("/settings", response_class=HTMLResponse)
def settings(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        return RedirectResponse(url="/login")
    return templates.TemplateResponse(request, "settings.html", {"active": "settings"})


@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(request, "login.html", {"active": "login"})


@app.get("/register", response_class=HTMLResponse)
def register_page(request: Request):
    return templates.TemplateResponse(request, "register.html", {"active": "register"})