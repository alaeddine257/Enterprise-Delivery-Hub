from __future__ import annotations

import os
import sqlite3
from typing import Any

import click
from flask import current_app, g


SCHEMA_FILE = os.path.join(os.path.dirname(__file__), "schema.sql")


def get_db() -> sqlite3.Connection:
    if "db" not in g:
        db_path = current_app.config["DATABASE_PATH"]
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        g.db = sqlite3.connect(db_path)
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(error: Exception | None = None) -> None:
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db() -> None:
    db = get_db()
    with open(SCHEMA_FILE, "r", encoding="utf-8") as file:
        db.executescript(file.read())
    db.commit()


@click.command("init-db")
def init_db_command() -> None:
    init_db()
    click.echo("Initialized the database.")


def query_db(query: str, args: tuple[Any, ...] = (), one: bool = False):
    db = get_db()
    cursor = db.execute(query, args)
    rows = cursor.fetchall()
    cursor.close()
    return (rows[0] if rows else None) if one else rows
