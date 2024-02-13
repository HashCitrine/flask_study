from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from controller import bp as exception_bp
from controller.tutorial_controller import bp as tutorial_bp


db = SQLAlchemy()
ma = Marshmallow()


def init_flask() -> Flask:
    flask = Flask(__name__)
    flask.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///python.db'

    db.init_app(flask)
    ma.init_app(flask)

    with flask.app_context():
        from controller.user_controller import bp as user_bp

        # db.drop_all()
        db.create_all()

        flask.register_blueprint(exception_bp)
        flask.register_blueprint(tutorial_bp)
        flask.register_blueprint(user_bp)

    return flask
