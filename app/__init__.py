from flask import Flask

from .extensions import DB
from .extensions import MIGRATE
from .config import Config
from .routes.user import USER
from .routes.post import POST
from .routes.main import MAIN

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(USER)
    app.register_blueprint(POST)
    app.register_blueprint(MAIN)

    DB.init_app(app)
    MIGRATE.init_app(app, DB)

    with app.app_context():
        DB.create_all()

    return app
