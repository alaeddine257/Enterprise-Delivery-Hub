import pytest
import app.validators as validators

def test_clean_text():
    assert validators.clean_text("  hello ") == "hello"
    assert validators.clean_text("") == ""
    assert validators.clean_text(None) == ""

def test_require_text():
    assert validators.require_text("  hi ") == "hi"
    assert validators.require_text("") is None
    assert validators.require_text(None) is None

def test_parse_float():
    assert validators.parse_float("3.14") == 3.14
    assert validators.parse_float("", 1.5) == 1.5
    assert validators.parse_float(None, 2.5) == 2.5
    assert validators.parse_float("not_a_number", 7.7) == 7.7

def test_parse_optional_int():
    assert validators.parse_optional_int("42") == 42
    assert validators.parse_optional_int("") is None
    assert validators.parse_optional_int(None) is None
    assert validators.parse_optional_int("not_a_number") is None

def test_as_payload():
    result = validators.as_payload(a=1, b=None, c="hi")
    assert result == {"a": 1, "c": "hi"}
