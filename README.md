# Enterprise Delivery Hub

An expanded enterprise-style delivery hub with Flask, SQLite, and a modern frontend. Modules include projects, departments, employees, tasks, risks, and reporting.

## Setup (Windows)

1. Create and activate venv:
   - `python -m venv .venv`
   - `.venv\Scripts\activate`

2. Install dependencies:
   - `pip install -r requirements.txt`

3. Initialize the database (re-run after schema updates):
   - `set FLASK_APP=run.py`
   - `flask init-db`

4. Run the app:
   - `python run.py`

Open http://127.0.0.1:5000

## Modules
- Dashboard
- Projects & updates
- Departments
- Employees
- Tasks
- Risks
- Reports

## API Endpoints
- /api/health
- /api/summary
- /api/projects
- /api/tasks
- /api/risks
