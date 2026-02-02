from __future__ import annotations

from flask import Blueprint, jsonify, request

from .services import (
    get_budget_stats,
    get_project_stats,
    get_recent_projects,
    get_recent_updates,
    get_risk_stats,
    get_task_stats,
    list_projects,
    list_risks,
    list_tasks,
    serialize_rows,
)

api = Blueprint("api", __name__, url_prefix="/api")


@api.get("/health")
def health():
    return jsonify({"status": "ok"})


@api.get("/summary")
def summary():
    return jsonify(
        {
            "projects": dict(get_project_stats() or {}),
            "tasks": dict(get_task_stats() or {}),
            "risks": dict(get_risk_stats() or {}),
            "budget": dict(get_budget_stats() or {}),
            "recent_projects": serialize_rows(get_recent_projects(6)),
            "recent_updates": serialize_rows(get_recent_updates(5)),
        }
    )


@api.get("/projects")
def projects():
    return jsonify(serialize_rows(list_projects()))


@api.get("/tasks")
def tasks():
    status = request.args.get("status")
    rows = list_tasks()
    if status:
        rows = [row for row in rows if row["status"] == status]
    return jsonify(serialize_rows(rows))


@api.get("/risks")
def risks():
    return jsonify(serialize_rows(list_risks()))
