from __future__ import annotations

from typing import Iterable

from .db import query_db


def get_project_stats():
    return query_db(
        """
        SELECT
            COUNT(*) AS total,
            SUM(CASE WHEN status = 'Backlog' THEN 1 ELSE 0 END) AS backlog,
            SUM(CASE WHEN status = 'In Progress' THEN 1 ELSE 0 END) AS in_progress,
            SUM(CASE WHEN status = 'At Risk' THEN 1 ELSE 0 END) AS at_risk,
            SUM(CASE WHEN status = 'Closed' THEN 1 ELSE 0 END) AS closed
        FROM projects
        """,
        one=True,
    )


def get_task_stats():
    return query_db(
        """
        SELECT
            COUNT(*) AS total,
            SUM(CASE WHEN status = 'Not Started' THEN 1 ELSE 0 END) AS not_started,
            SUM(CASE WHEN status = 'In Progress' THEN 1 ELSE 0 END) AS in_progress,
            SUM(CASE WHEN status = 'Blocked' THEN 1 ELSE 0 END) AS blocked,
            SUM(CASE WHEN status = 'Done' THEN 1 ELSE 0 END) AS done
        FROM tasks
        """,
        one=True,
    )


def get_risk_stats():
    return query_db(
        """
        SELECT
            COUNT(*) AS total,
            SUM(CASE WHEN status = 'Open' THEN 1 ELSE 0 END) AS open,
            SUM(CASE WHEN status = 'Mitigated' THEN 1 ELSE 0 END) AS mitigated,
            SUM(CASE WHEN status = 'Accepted' THEN 1 ELSE 0 END) AS accepted
        FROM risks
        """,
        one=True,
    )


def get_recent_projects(limit: int = 6):
    return query_db(
        """
        SELECT projects.id, projects.name, projects.owner, projects.status, projects.created_at,
               departments.name AS department
        FROM projects
        LEFT JOIN departments ON departments.id = projects.department_id
        ORDER BY projects.created_at DESC
        LIMIT ?
        """,
        (limit,),
    )


def get_recent_updates(limit: int = 5):
    return query_db(
        """
        SELECT updates.summary, updates.created_at, projects.name AS project_name
        FROM updates
        JOIN projects ON projects.id = updates.project_id
        ORDER BY updates.created_at DESC
        LIMIT ?
        """,
        (limit,),
    )


def get_upcoming_tasks(limit: int = 5):
    return query_db(
        """
        SELECT tasks.title, tasks.due_date, tasks.status, projects.name AS project_name
        FROM tasks
        JOIN projects ON projects.id = tasks.project_id
        WHERE tasks.status != 'Done' AND tasks.due_date IS NOT NULL AND tasks.due_date != ''
        ORDER BY tasks.due_date ASC
        LIMIT ?
        """,
        (limit,),
    )


def get_open_risks(limit: int = 5):
    return query_db(
        """
        SELECT risks.title, risks.impact, risks.likelihood, projects.name AS project_name
        FROM risks
        JOIN projects ON projects.id = risks.project_id
        WHERE risks.status = 'Open'
        ORDER BY risks.created_at DESC
        LIMIT ?
        """,
        (limit,),
    )


def get_status_breakdowns():
    return query_db(
        """
        SELECT status, COUNT(*) AS total
        FROM projects
        GROUP BY status
        ORDER BY total DESC
        """
    )


def get_task_breakdowns():
    return query_db(
        """
        SELECT status, COUNT(*) AS total
        FROM tasks
        GROUP BY status
        ORDER BY total DESC
        """
    )


def get_risk_breakdowns():
    return query_db(
        """
        SELECT status, COUNT(*) AS total
        FROM risks
        GROUP BY status
        ORDER BY total DESC
        """
    )


def get_budget_stats():
    return query_db(
        """
        SELECT
            COUNT(*) AS total_projects,
            SUM(budget) AS total_budget,
            AVG(budget) AS avg_budget
        FROM projects
        """,
        one=True,
    )


def list_projects():
    return query_db(
        """
        SELECT projects.id, projects.name, projects.owner, projects.status, projects.budget,
               projects.created_at, departments.name AS department
        FROM projects
        LEFT JOIN departments ON departments.id = projects.department_id
        ORDER BY projects.created_at DESC
        """
    )


def list_tasks():
    return query_db(
        """
        SELECT tasks.id, tasks.title, tasks.priority, tasks.status, tasks.due_date,
               projects.name AS project_name, employees.full_name AS assignee
        FROM tasks
        JOIN projects ON projects.id = tasks.project_id
        LEFT JOIN employees ON employees.id = tasks.assignee_id
        ORDER BY tasks.created_at DESC
        """
    )


def list_risks():
    return query_db(
        """
        SELECT risks.id, risks.title, risks.impact, risks.likelihood, risks.mitigation,
               risks.status, risks.created_at, projects.name AS project_name
        FROM risks
        JOIN projects ON projects.id = risks.project_id
        ORDER BY risks.created_at DESC
        """
    )


def list_departments():
    return query_db(
        """
        SELECT id, name, head, created_at
        FROM departments
        ORDER BY name ASC
        """
    )


def list_employees():
    return query_db(
        """
        SELECT employees.id, employees.full_name, employees.email, employees.role,
               employees.created_at, departments.name AS department
        FROM employees
        LEFT JOIN departments ON departments.id = employees.department_id
        ORDER BY employees.created_at DESC
        """
    )


def serialize_rows(rows: Iterable):
    return [dict(row) for row in rows]
