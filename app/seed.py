from datetime import datetime
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.db import get_db

def seed():
    import sqlite3
    from datetime import datetime, timezone
    db = get_db()
    now = datetime.now(timezone.utc).isoformat()
    # Departments
    departments = [
        ("Technology", "Fatima G.", now),
        ("Finance", "Ali B.", now),
        ("HR", "Mouna S.", now),
        ("Operations", "Karim T.", now),
        ("Sales", "Nadia M.", now),
    ]
    for name, head, created in departments:
        try:
            db.execute("INSERT INTO departments (name, head, created_at) VALUES (?, ?, ?)", (name, head, created))
        except sqlite3.IntegrityError:
            pass  # Skip if already exists

    # Employees
    employees = [
        ("Rami K.", "rami@company.com", "Product Manager", 1, now),
        ("Sara L.", "sara@company.com", "Engineer", 1, now),
        ("Omar B.", "omar@company.com", "Accountant", 2, now),
        ("Lina P.", "lina@company.com", "HR Specialist", 3, now),
        ("Yassine D.", "yassine@company.com", "Ops Lead", 4, now),
        ("Sami F.", "sami@company.com", "Sales Rep", 5, now),
        ("A. Damak", "alaeddine@company.com", "CTO", 1, now),
        ("Fatima G.", "fatima@company.com", "CFO", 2, now),
        ("Ali B.", "ali@company.com", "CEO", 2, now),
        ("Mouna S.", "mouna@company.com", "HR Director", 3, now),
    ]
    for full_name, email, role, dept_id, created in employees:
        try:
            db.execute("INSERT INTO employees (full_name, email, role, department_id, created_at) VALUES (?, ?, ?, ?, ?)", (full_name, email, role, dept_id, created))
        except sqlite3.IntegrityError:
            pass  # Skip if already exists

    # Projects
    projects = [
        ("Core Banking Upgrade", "A. Damak", "In Progress", 1, 50000, now),
        ("ERP Rollout", "Fatima G.", "Backlog", 2, 30000, now),
        ("HR System Revamp", "Mouna S.", "At Risk", 3, 20000, now),
        ("Cloud Migration", "Yassine D.", "In Progress", 4, 40000, now),
        ("CRM Launch", "Sami F.", "Backlog", 5, 25000, now),
        ("Payroll Automation", "Lina P.", "Closed", 3, 15000, now),
        ("Expense Tracker", "Omar B.", "In Progress", 2, 12000, now),
        ("Sales Dashboard", "Nadia M.", "At Risk", 5, 18000, now),
    ]
    for name, owner, status, dept_id, budget, created in projects:
        db.execute("INSERT INTO projects (name, owner, status, department_id, budget, created_at) VALUES (?, ?, ?, ?, ?, ?)", (name, owner, status, dept_id, budget, created))

    # Tasks
    tasks = [
        (1, "Prepare vendor RFP", 1, "High", "In Progress", now[:10], now),
        (2, "Data migration plan", 2, "Medium", "Not Started", now[:10], now),
        (3, "Draft HR policy", 4, "High", "Blocked", now[:10], now),
        (4, "Set up cloud infra", 5, "Critical", "In Progress", now[:10], now),
        (5, "Import leads", 6, "Medium", "Not Started", now[:10], now),
        (6, "Payroll test run", 7, "Low", "Done", now[:10], now),
        (7, "Expense API integration", 3, "High", "In Progress", now[:10], now),
        (8, "Sales data sync", 8, "Medium", "Blocked", now[:10], now),
        (1, "Finalize contract", 2, "Critical", "Not Started", now[:10], now),
        (2, "ERP user training", 9, "Medium", "In Progress", now[:10], now),
    ]
    for project_id, title, assignee_id, priority, status, due_date, created in tasks:
        db.execute("INSERT INTO tasks (project_id, title, assignee_id, priority, status, due_date, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)", (project_id, title, assignee_id, priority, status, due_date, created))

    # Risks
    risks = [
        (1, "Vendor onboarding delay", "High", "Medium", "Escalate resource approval", "Open", now),
        (3, "HR system compliance", "Medium", "High", "Legal review", "Mitigated", now),
        (4, "Cloud cost overrun", "High", "High", "Budget alerts", "Open", now),
        (5, "CRM data loss", "Critical", "Low", "Daily backup", "Accepted", now),
        (7, "Expense fraud", "High", "Medium", "Audit logs", "Open", now),
    ]
    for project_id, title, impact, likelihood, mitigation, status, created in risks:
        db.execute("INSERT INTO risks (project_id, title, impact, likelihood, mitigation, status, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)", (project_id, title, impact, likelihood, mitigation, status, created))

    # Updates
    updates = [
        (1, "Kickoff completed.", now),
        (2, "ERP vendor selected.", now),
        (3, "HR policy draft submitted.", now),
        (4, "Cloud infra 50% done.", now),
        (5, "CRM requirements gathered.", now),
        (6, "Payroll automation live.", now),
        (7, "Expense tracker MVP ready.", now),
        (8, "Sales dashboard wireframe approved.", now),
    ]
    for project_id, summary, created in updates:
        db.execute("INSERT INTO updates (project_id, summary, created_at) VALUES (?, ?, ?)", (project_id, summary, created))

    db.commit()

if __name__ == "__main__":
    from app import create_app
    app = create_app()
    with app.app_context():
        seed()
    print("Database seeded with sample data.")
