# TaskFlow

A modern task management web app built with FastAPI, Jinja2, HTMX, SQLAlchemy and PostgreSQL.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-latest-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-18-blue)

## Tech Stack

- **FastAPI** — Python web framework
- **Jinja2** — Server-side HTML templating
- **HTMX** — Dynamic UI updates without JavaScript
- **SQLAlchemy** — Database ORM
- **PostgreSQL** — Database
- **Alembic** — Database migrations
- **JWT (python-jose)** — Authentication tokens
- **Passlib (bcrypt)** — Password hashing

## Features

- ✅ User registration and login
- ✅ JWT authentication with cookies
- ✅ Tasks scoped per user
- ✅ Create and delete tasks
- ✅ Mark tasks as completed
- ✅ Completed tasks view
- ✅ Modern dark UI with sidebar navigation
- ✅ Dynamic updates without page reloads (HTMX)
- ✅ Database migrations with Alembic
- ✅ Protected routes with auth redirect

## Project Structure

```
fastapi-task-manager/
├── app/
│   ├── main.py               # App entry point and routes
│   ├── database.py           # Database connection
│   ├── models.py             # SQLAlchemy table definitions
│   ├── schemas.py            # Pydantic validation
│   ├── auth.py               # JWT and password utilities
│   ├── routers/
│   │   ├── tasks.py          # Task endpoints
│   │   └── auth.py           # Auth endpoints
│   └── templates/
│       ├── base.html         # Shared layout
│       ├── index.html        # My Tasks page
│       ├── completed.html    # Completed page
│       ├── settings.html     # Settings page
│       ├── login.html        # Login page
│       ├── register.html     # Register page
│       └── partials/
│           └── task_list.html
├── alembic/                  # Database migrations
├── .env                      # Environment variables (not committed)
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.13+
- PostgreSQL

### Installation

1. Clone the repo
```bash
git clone https://github.com/MbIndaz/fastapi-task-manager.git
cd fastapi-task-manager
```

2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create a `.env` file:
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/taskmanager

SECRET_KEY=your-secret-key-here

5. Create the database
```bash
psql -U postgres -c "CREATE DATABASE taskmanager;"
```

6. Run migrations
```bash
alembic upgrade head
```

7. Run the app
```bash
uvicorn app.main:app --reload
```

8. Open your browser at `http://127.0.0.1:8000`

## API Docs

FastAPI automatically generates interactive API documentation at:
`http://127.0.0.1:8000/docs`

## Database Migrations

Alembic handles all database schema changes. To create a new migration after changing models:

```bash
alembic revision --autogenerate -m "description of change"
alembic upgrade head
```

## Author

Miguel — [GitHub](https://github.com/MbIndaz)