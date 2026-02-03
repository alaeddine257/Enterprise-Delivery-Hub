import pytest
from app import create_app
from app import seed as seed_module

@pytest.fixture
def app_context():
    app = create_app()
    with app.app_context():
        yield

def test_seed_runs_without_error(app_context):
    # Should not raise any exceptions
    seed_module.seed()

def test_seed_idempotency(app_context):
    # Running seed twice should not raise due to IntegrityError handling
    seed_module.seed()
    seed_module.seed()
