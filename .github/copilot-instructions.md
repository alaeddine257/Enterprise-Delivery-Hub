# Copilot Instructions for Enterprise Delivery Hub

## Build, Test, and Lint Commands

- **Install dependencies:**
  ```sh
  pip install -r requirements.txt
  ```
- **Initialize the database:**
  ```sh
  flask init-db
  ```
- **Run the app (development):**
  ```sh
  python run.py
  ```
- **No test or lint commands are currently defined.**

## High-Level Architecture

- **Framework:** Flask (Python)
- **Database:** SQLite (schema in `app/schema.sql`, managed via `app/db.py`)
- **App Factory:** `create_app()` in `app/__init__.py` sets up the Flask app, registers blueprints, and configures the database.
- **Blueprints:**
  - Main UI routes: `app/routes.py` (registered as `main_bp`)
  - API endpoints: `app/api.py` (registered as `api_bp`, all under `/api`)
- **Services Layer:** `app/services.py` provides data access and aggregation for projects, tasks, risks, etc.
- **Validation:** `app/validators.py` handles input validation and parsing.
- **Database Access:**
  - `app/db.py` manages connections, schema, and queries.
  - `app/seed.py` can populate the database with initial data.
- **Frontend:**
  - HTML templates in `templates/`
  - Static assets in `static/`

## Key Conventions

- **Database Path:** Set via `DATABASE_PATH` in app config (default: `database/app.db`).
- **Schema Management:** Use `flask init-db` to (re)initialize the database from `app/schema.sql`.
- **Blueprints:** All UI routes are in `app/routes.py`; all API endpoints are in `app/api.py`.
- **API:** All API endpoints are prefixed with `/api`.
- **No built-in test or linting framework is present.**

---

This file was generated to help Copilot and other AI assistants understand the structure and conventions of this repository. If you want to adjust or expand coverage, or add test/lint instructions, let me know!