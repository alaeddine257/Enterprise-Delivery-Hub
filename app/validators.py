from __future__ import annotations

from typing import Any


def clean_text(value: str | None) -> str:
    return (value or "").strip()


def require_text(value: str | None) -> str | None:
    cleaned = clean_text(value)
    return cleaned if cleaned else None


def parse_float(value: str | None, default: float = 0.0) -> float:
    try:
        return float(value) if value not in (None, "") else default
    except ValueError:
        return default


def parse_optional_int(value: str | None) -> int | None:
    if value in (None, ""):
        return None
    try:
        return int(value)
    except ValueError:
        return None


def as_payload(**kwargs: Any) -> dict[str, Any]:
    return {key: value for key, value in kwargs.items() if value is not None}
