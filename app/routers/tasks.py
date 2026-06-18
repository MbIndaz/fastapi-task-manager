from fastapi import APIRouter, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from app.auth import get_current_user
from typing import Optional

router = APIRouter(prefix="/tasks", tags=["tasks"])
templates = Jinja2Templates(directory="app/templates")

def render_task_list(request: Request, db: Session, user: models.User, completed_only: bool = False, exclude_completed: bool = False):
    query = db.query(models.Task).filter(models.Task.owner_id == user.id)
    if completed_only:
        query = query.filter(models.Task.completed == True)
    if exclude_completed:
        query = query.filter(models.Task.completed == False)
    tasks = query.all()
    return templates.TemplateResponse(request, "partials/task_list.html", {"tasks": tasks})

@router.get("/html", response_class=HTMLResponse)
def get_tasks_html(request: Request, db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    return render_task_list(request, db, user, exclude_completed=True)

@router.get("/completed", response_class=HTMLResponse)
def get_completed_html(request: Request, db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    tasks = db.query(models.Task).filter(models.Task.owner_id == user.id, models.Task.completed == True).all()
    return templates.TemplateResponse(request, "partials/task_list.html", {"tasks": tasks, "show_completed": True})

@router.get("/", response_model=list[schemas.TaskResponse])
def get_tasks(db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    return db.query(models.Task).filter(models.Task.owner_id == user.id).all()

@router.post("/", response_class=HTMLResponse)
def create_task(request: Request, title: str = Form(...), description: Optional[str] = Form(None),
                 db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    db_task = models.Task(title=title, description=description, owner_id=user.id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return render_task_list(request, db, user)

@router.delete("/{task_id}", response_class=HTMLResponse)
def delete_task(request: Request, task_id: int, db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id, models.Task.owner_id == user.id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    was_completed = db_task.completed
    db.delete(db_task)
    db.commit()
    if was_completed:
        tasks = db.query(models.Task).filter(models.Task.owner_id == user.id, models.Task.completed == True).all()
        return templates.TemplateResponse(request, "partials/task_list.html", {"tasks": tasks, "show_completed": True})
    return render_task_list(request, db, user, exclude_completed=True)

@router.patch("/{task_id}", response_class=HTMLResponse)
def update_task(request: Request, task_id: int, db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id, models.Task.owner_id == user.id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    db_task.completed = True
    db.commit()
    return render_task_list(request, db, user, completed_only=False, exclude_completed=True)