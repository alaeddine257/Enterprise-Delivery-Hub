import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_project_missing_fields(client):
    response = client.post("/projects", data={})
    # Should redirect due to missing name/owner
    assert response.status_code in (302, 308)

def test_create_department_missing_fields(client):
    response = client.post("/departments", data={})
    assert response.status_code in (302, 308)

def test_create_employee_missing_fields(client):
    response = client.post("/employees", data={})
    assert response.status_code in (302, 308)

def test_create_task_missing_fields(client):
    response = client.post("/tasks", data={})
    assert response.status_code in (302, 308)

def test_create_risk_missing_fields(client):
    response = client.post("/risks", data={})
    assert response.status_code in (302, 308)

def test_mark_task_done_invalid(client):
    # Try to mark a non-existent task as done
    response = client.post("/tasks/99999/done")
    assert response.status_code in (302, 308)

def test_mitigate_risk_invalid(client):
    # Try to mitigate a non-existent risk
    response = client.post("/risks/99999/mitigate")
    assert response.status_code in (302, 308)

def test_reports_route(client):
    response = client.get("/reports")
    assert response.status_code == 200
    assert b"<html" in response.data
