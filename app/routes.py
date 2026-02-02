from __future__ import annotations

from datetime import datetime

from flask import Blueprint, redirect, render_template, request, url_for

from .db import get_db
from .services import (
    get_budget_stats,
    get_open_risks,
    get_project_stats,
    get_recent_projects,
    get_recent_updates,
    get_risk_breakdowns,
    get_risk_stats,
    get_status_breakdowns,
    get_task_breakdowns,
    get_task_stats,
    get_upcoming_tasks,
    list_departments,
    list_employees,
    list_projects,
    list_risks,
    list_tasks,
)
from .validators import parse_float, parse_optional_int, require_text

bp = Blueprint("main", __name__)


@bp.before_app_request
def ensure_db():
    db = get_db()
    db.execute("PRAGMA journal_mode=WAL")
    db.execute("PRAGMA foreign_keys=ON")


@bp.route("/", methods=["GET"])
def dashboard():
    project_stats = get_project_stats()
    task_stats = get_task_stats()
    risk_stats = get_risk_stats()
    recent_projects = get_recent_projects(6)
    recent_updates = get_recent_updates(5)
    upcoming_tasks = get_upcoming_tasks(5)
    open_risks = get_open_risks(5)

    return render_template(
        "index.html",
        project_stats=project_stats,
        task_stats=task_stats,
        risk_stats=risk_stats,
        recent_projects=recent_projects,
        recent_updates=recent_updates,
        upcoming_tasks=upcoming_tasks,
        open_risks=open_risks,
    )


@bp.route("/projects", methods=["GET"])
def projects():
    departments = list_departments()
    projects = list_projects()
    return render_template("projects.html", projects=projects, departments=departments)


@bp.route("/projects", methods=["POST"])
def create_project():
    name = require_text(request.form.get("name"))
    owner = require_text(request.form.get("owner"))
    status = require_text(request.form.get("status")) or "Backlog"
    department_id = parse_optional_int(request.form.get("department_id"))
    budget = parse_float(request.form.get("budget"), 0.0)

    if not name or not owner:
        return redirect(url_for("main.projects"))

    db = get_db()
    db.execute(
        """
        INSERT INTO projects (name, owner, status, department_id, budget, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (name, owner, status, department_id, budget, datetime.utcnow().isoformat()),
    )
    db.commit()
    return redirect(url_for("main.projects"))


@bp.route("/projects/<int:project_id>/close", methods=["POST"])
def close_project(project_id: int):
    db = get_db()
    db.execute("UPDATE projects SET status = ? WHERE id = ?", ("Closed", project_id))
    db.commit()
    return redirect(url_for("main.projects"))


@bp.route("/projects/<int:project_id>/updates", methods=["POST"])
def add_project_update(project_id: int):
    summary = require_text(request.form.get("summary"))
    if not summary:
        return redirect(url_for("main.projects"))
    db = get_db()
    db.execute(
        """
        INSERT INTO updates (project_id, summary, created_at)
        VALUES (?, ?, ?)
        """,
        (project_id, summary, datetime.utcnow().isoformat()),
    )
    db.commit()
    return redirect(url_for("main.projects"))


@bp.route("/departments", methods=["GET"])
def departments():
    departments = list_departments()
    return render_template("departments.html", departments=departments)


@bp.route("/departments", methods=["POST"])
def create_department():
    name = require_text(request.form.get("name"))
    head = require_text(request.form.get("head"))
    if not name or not head:
        return redirect(url_for("main.departments"))
    db = get_db()
    db.execute(
        """
        INSERT INTO departments (name, head, created_at)
        VALUES (?, ?, ?)
        """,
        (name, head, datetime.utcnow().isoformat()),
    )
    db.commit()
    return redirect(url_for("main.departments"))


@bp.route("/employees", methods=["GET"])
def employees():
    departments = list_departments()
    employees = list_employees()
    return render_template("employees.html", employees=employees, departments=departments)


@bp.route("/employees", methods=["POST"])
def create_employee():
    full_name = require_text(request.form.get("full_name"))
    email = require_text(request.form.get("email"))
    role = require_text(request.form.get("role"))
    department_id = parse_optional_int(request.form.get("department_id"))
    if not full_name or not email or not role:
        return redirect(url_for("main.employees"))
    db = get_db()
    db.execute(
        """
        INSERT INTO employees (full_name, email, role, department_id, created_at)
        VALUES (?, ?, ?, ?, ?)
        """,
        (full_name, email, role, department_id, datetime.utcnow().isoformat()),
    )
    db.commit()
    return redirect(url_for("main.employees"))


@bp.route("/tasks", methods=["GET"])
def tasks():
    projects = list_projects()
    employees = list_employees()
    tasks = list_tasks()
    return render_template(
        "tasks.html",
        tasks=tasks,
        projects=projects,
        employees=employees,
    )


@bp.route("/tasks", methods=["POST"])
def create_task():
    title = require_text(request.form.get("title"))
    project_id = parse_optional_int(request.form.get("project_id"))
    assignee_id = parse_optional_int(request.form.get("assignee_id"))
    priority = require_text(request.form.get("priority")) or "Medium"
    status = require_text(request.form.get("status")) or "Not Started"
    due_date = require_text(request.form.get("due_date")) or ""
    if not title or not project_id:
        return redirect(url_for("main.tasks"))
    db = get_db()
    db.execute(
        """
        INSERT INTO tasks (project_id, title, assignee_id, priority, status, due_date, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (project_id, title, assignee_id, priority, status, due_date, datetime.utcnow().isoformat()),
    )
    db.commit()
    return redirect(url_for("main.tasks"))


@bp.route("/tasks/<int:task_id>/done", methods=["POST"])
def mark_task_done(task_id: int):
    db = get_db()
    db.execute("UPDATE tasks SET status = ? WHERE id = ?", ("Done", task_id))
    db.commit()
    return redirect(url_for("main.tasks"))


@bp.route("/risks", methods=["GET"])
def risks():
    projects = list_projects()
    risks = list_risks()
    return render_template("risks.html", risks=risks, projects=projects)


@bp.route("/risks", methods=["POST"])
def create_risk():
    project_id = parse_optional_int(request.form.get("project_id"))
    title = require_text(request.form.get("title"))
    impact = require_text(request.form.get("impact")) or "Medium"
    likelihood = require_text(request.form.get("likelihood")) or "Medium"
    mitigation = require_text(request.form.get("mitigation"))
    status = require_text(request.form.get("status")) or "Open"
    if not project_id or not title or not mitigation:
        return redirect(url_for("main.risks"))
    db = get_db()
    db.execute(
        """
        INSERT INTO risks (project_id, title, impact, likelihood, mitigation, status, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            project_id,
            title,
            impact,
            likelihood,
            mitigation,
            status,
            datetime.utcnow().isoformat(),
        ),
    )
    db.commit()
    return redirect(url_for("main.risks"))


@bp.route("/risks/<int:risk_id>/mitigate", methods=["POST"])
def mitigate_risk(risk_id: int):
    db = get_db()
    db.execute("UPDATE risks SET status = ? WHERE id = ?", ("Mitigated", risk_id))
    db.commit()
    return redirect(url_for("main.risks"))


@bp.route("/reports", methods=["GET"])
def reports():
    status_breakdown = get_status_breakdowns()
    task_breakdown = get_task_breakdowns()
    risk_breakdown = get_risk_breakdowns()
    budget_stats = get_budget_stats()
    return render_template(
        "reports.html",
        status_breakdown=status_breakdown,
        task_breakdown=task_breakdown,
        risk_breakdown=risk_breakdown,
        budget_stats=budget_stats,
    )
