# Enterprise Delivery Hub

An expanded enterprise-style delivery hub with Flask, SQLite, and a modern frontend. Modules include projects, departments, employees, tasks, risks, and reporting.

## Prerequisites

Before launching the application, ensure you have the following installed:

- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
  - Verify installation: `python --version` or `python3 --version`
- **pip** (Python package manager) - Usually included with Python
  - Verify installation: `pip --version` or `pip3 --version`
- **Git** (optional, for cloning the repository) - [Download Git](https://git-scm.com/downloads)

## How to Launch This App

### Step 1: Clone or Download the Repository

If you haven't already, get the code:

```bash
# Option A: Clone with Git
git clone https://github.com/alaeddine257/Enterprise-Delivery-Hub.git
cd Enterprise-Delivery-Hub

# Option B: Download and extract the ZIP file, then navigate to the folder
```

### Step 2: Create a Virtual Environment

A virtual environment isolates the project dependencies from your system Python.

#### On Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

#### On macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Note:** After activation, you should see `(.venv)` at the beginning of your command prompt.

### Step 3: Install Dependencies

With the virtual environment activated, install the required packages:

```bash
pip install -r requirements.txt
```

This will install Flask and other necessary dependencies.

### Step 4: Initialize the Database

The application uses SQLite for data storage. Initialize the database with the schema:

#### On Windows:
```bash
set FLASK_APP=run.py
flask init-db
```

#### On macOS/Linux:
```bash
export FLASK_APP=run.py
flask init-db
```

You should see the message: `Initialized the database.`

**Note:** Re-run this command whenever the database schema is updated.

### Step 5: Run the Application

Start the Flask development server:

```bash
python run.py
```

You should see output similar to:
```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

### Step 6: Access the Application

Open your web browser and navigate to:

**http://127.0.0.1:5000** or **http://localhost:5000**

You should see the Enterprise Delivery Hub dashboard.

## Quick Start (All Platforms)

For experienced users, here's a quick command sequence:

### Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
set FLASK_APP=run.py
flask init-db
python run.py
```

### macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=run.py
flask init-db
python run.py
```

Then open http://127.0.0.1:5000 in your browser.

## Stopping the Application

To stop the Flask server, press `CTRL+C` in the terminal where the app is running.

## Deactivating the Virtual Environment

When you're done working with the application, deactivate the virtual environment:

```bash
deactivate
```

## Troubleshooting

### Issue: `python: command not found` or `python3: command not found`

**Solution:** 
- Ensure Python is installed and added to your system PATH
- On some systems, use `python3` instead of `python`
- On Windows, you may need to use `py` instead of `python`

### Issue: `pip: command not found`

**Solution:**
- Try `python -m pip` or `python3 -m pip` instead of just `pip`
- Ensure pip is installed: `python -m ensurepip --upgrade`

### Issue: Permission denied when creating virtual environment

**Solution:**
- On Windows, run the command prompt as Administrator
- On macOS/Linux, check folder permissions: `chmod +w .`

### Issue: `flask: command not found` after installing requirements

**Solution:**
- Ensure the virtual environment is activated (you should see `(.venv)` in your prompt)
- Try using: `python -m flask init-db` instead of `flask init-db`

### Issue: Port 5000 is already in use

**Solution:**
- Stop any other applications using port 5000
- Or modify `run.py` to use a different port:
  ```python
  app.run(debug=True, port=5001)
  ```

### Issue: Database errors or missing tables

**Solution:**
- Re-initialize the database: Run the `flask init-db` command again
- Delete the `database/app.db` file and re-run `flask init-db`

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
