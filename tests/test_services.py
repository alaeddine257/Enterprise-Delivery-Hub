import pytest
import app.services as services

def test_service_functions_exist():
    # Check for actual service functions
    assert hasattr(services, 'get_project_stats')
    assert hasattr(services, 'get_task_stats')
    assert hasattr(services, 'get_risk_stats')
    assert hasattr(services, 'list_projects')
    assert hasattr(services, 'list_tasks')
