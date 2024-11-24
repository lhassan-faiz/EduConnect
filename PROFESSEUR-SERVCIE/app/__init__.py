from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)

    from app.routes import professor_bp
    app.register_blueprint(professor_bp, url_prefix="/api/v1/professors")

    return app

