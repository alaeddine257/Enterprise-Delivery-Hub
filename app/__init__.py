from flask import Flask

from .api import api as api_bp
from .db import close_db, init_db_command
from .routes import bp as main_bp


import os

def create_app():
    base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    template_dir = os.path.join(base_dir, "templates")
    static_dir = os.path.join(base_dir, "static")
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
    app.config.from_mapping(
        DATABASE_PATH="database/app.db",
        SECRET_KEY="change-me",
    )

    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)
    app.cli.add_command(init_db_command)
    app.teardown_appcontext(close_db)

    return app
