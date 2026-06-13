from fastapi import APIRouter, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from typing import Optional

router = APIRouter(prefix="/tasks", tags=["tasks"])
templates = Jinja2Templates(directory="app/templates")

def render_task_list(request: Request, db: Session):
    tasks = db.query(models.Task).all()
    return templates.TemplateResponse(request, "partials/task_list.html", {"tasks": tasks})

@router.get("/html", response_class=HTMLResponse)
def get_tasks_html(request: Request, db: Session = Depends(get_db)):
    return render_task_list(request, db)

@router.get("/", response_model=list[schemas.TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()

@router.post("/", response_class=HTMLResponse)
def create_task(request: Request, title: str = Form(...), description: Optional[str] = Form(None), db: Session = Depends(get_db)):
    db_task = models.Task(title=title, description=description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return render_task_list(request, db)

@router.delete("/{task_id}", response_class=HTMLResponse)
def delete_task(request: Request, task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(db_task)
    db.commit()
    return render_task_list(request, db)

@router.patch("/{task_id}", response_class=HTMLResponse)
def update_task(request: Request, task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    db_task.completed = True
    db.commit()
    return render_task_list(request, db)