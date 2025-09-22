# 📝 Task List API

A simple **CRUD REST API** built with **Flask**, **SQLAlchemy**, **Flask-Migrate**, **Marshmallow**, and **Flask-Smorest** — complete with **Swagger UI** documentation.

This project is my very first API! 🎉  
It demonstrates:
- 🏗️ **Flask** application factory pattern
- 📦 **SQLAlchemy** ORM models
- 🔄 **Database migrations** with Flask-Migrate (Alembic)
- ✅ **Request validation & serialization** with Marshmallow
- 📚 **Interactive API docs** via Swagger UI (OpenAPI 3)
- 🗃️ **SQLite** (easily switchable to MySQL/PostgreSQL)

---

## 🚀 Features

- **CRUD endpoints** for tasks:
  - Create a task
  - Read all tasks or a single one
  - Update (partial or full)
  - Soft delete (mark as deleted, not permanently removed)
- **Automatic OpenAPI docs** available at `/docs`
- **Validation & error handling** (e.g. unique name constraint → HTTP 409)
- **Timestamps**: `created_at`, `updated_at`
- **Soft delete**: keeps data but hides from main listing

---

## 🛠 Tech Stack

- **Backend:** Flask 3, Flask-Smorest, SQLAlchemy
- **Validation/Serialization:** Marshmallow
- **Migrations:** Flask-Migrate (Alembic)
- **Database:** SQLite (local dev) — easy to switch to MySQL
- **Docs:** Swagger UI (auto-generated from schemas)

---

## 📂 Project Structure

task_api_flask/
├── app.py # Application factory & entry point
├── config.py # Configuration classes (dev, default)
├── db.py # SQLAlchemy instance
├── models.py # Task model (ORM)
├── schemas.py # Marshmallow schemas (validation/serialization)
├── resources/
│ ├── init.py # Package marker
│ └── tasks.py # Task routes (Blueprint)
├── migrations/ # Alembic migration scripts
├── taskapi.sqlite # SQLite database (auto-created after migration)
├── requirements.txt # Dependencies
└── README.md # This file

---

## ⚡ Getting Started

### 1. Clone & Install
```bash
git clone https://github.com/YOUR-USERNAME/task_api_flask.git
cd task_api_flask
python -m venv .venv
# Activate venv (Windows PowerShell)
. .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

## Set Environment Variables

$env:FLASK_APP = "app.py"
$env:FLASK_CONFIG = "dev"

## Initialize Database

flask db init
flask db migrate -m "create tasks table"
flask db upgrade

## Run the Server

flask run

## Visit: http://127.0.0.1:5000/docs
 to explore Swagger UI.

##🧪 Next Steps / Ideas

✅ Add pagination and filtering (e.g. ?completed=true)
🔑 Add authentication (JWT)
🐳 Dockerize (API + MySQL container)
🧾 CI/CD with GitHub Actions

## 🙌 Acknowledgements

This API was built as a personal learning project — my first API with Flask!
Thanks to Flask, Marshmallow, and Swagger for making it a joy to work with. ❤️
