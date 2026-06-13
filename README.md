# FastAPI Task Manager

A task management web app built with FastAPI, Jinja2 templates, and HTMX for dynamic page updates without a JavaScript framework.

## Tech Stack

- **FastAPI** — Python web framework
- **Jinja2** — Server-side HTML templating
- **HTMX** — Dynamic UI updates without writing JavaScript
- **SQLAlchemy** — Database ORM
- **PostgreSQL** — Database
- **Alembic** — Database migrations

## Features

- Create and delete tasks
- Real-time page updates via HTMX (no full page reloads)
- RESTful API endpoints

## Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL

### Installation

```bash
# Clone the repo
git clone https://github.com/MbIndaz/fastapi-task-manager
cd fastapi-task-manager

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment variables
cp .env.example .env
# Edit .env with your database credentials

# Run the app
uvicorn main:app --reload
```

Open http://localhost:8000

## Project Structure

```
fastapi-task-manager/
├── main.py
├── templates/
│   ├── base.html
│   ├── index.html
│   └── partials/
│       └── task_list.html
├── requirements.txt
└── .env.example
```
