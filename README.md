# FastAPI Task Manager

A task management web app built with FastAPI, Jinja2 templates, and HTMX for dynamic page updates without a JavaScript framework.

## Tech Stack

- **FastAPI** — Python web framework
- **Jinja2** — Server-side HTML templating
- **HTMX** — Dynamic UI updates without JavaScript
- **SQLAlchemy** — Database ORM
- **PostgreSQL** — Database
- **Alembic** — Database migrations

## Features

-  Create and delete tasks
-  Mark tasks as completed
-  Completed tasks view
-  Modern dark UI with sidebar navigation
-  Dynamic updates without page reloads (HTMX)
-  Database migrations with Alembic

## Getting Started

### Prerequisites

- Python 3.10+
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

4. Set up environment variables — create a `.env` file:
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/taskmanager

5. Create the database
```bash
psql -U postgres -c "CREATE DATABASE taskmanager;"
```

6. Run the app
```bash
uvicorn app.main:app --reload
```

7. Open your browser at `http://127.0.0.1:8000`

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

## Project Structure

```
fastapi-task-manager/
├── app/
│   ├── main.py             # App entry point and routes
│   ├── database.py         # Database connection
│   ├── models.py           # SQLAlchemy table definitions
│   ├── schemas.py          # Pydantic validation
│   ├── routers/
│   │   └── tasks.py        # Task endpoints
│   └── templates/
│       ├── base.html       # Shared layout
│       ├── index.html      # My Tasks page
│       ├── completed.html  # Completed page
│       ├── settings.html   # Settings page
│       └── partials/
│           └── task_list.html
├── .env
├── requirements.txt
└── README.md
```
