import pytest
from app import db

import pytest
from app import create_app
from app import db

@pytest.fixture
def app_context():
    app = create_app()
    with app.app_context():
        yield

def test_db_connection(app_context):
    conn = db.get_db()
    assert conn is not None
    conn.close()
