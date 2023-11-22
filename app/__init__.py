# app/__init__.py
import logging
from flask import Flask
from flask import has_request_context, request
from flask.logging import default_handler

class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None

        return super().format(record)


# mail_handler.setFormatter(formatter)


def create_app():
    app = Flask(__name__)
    app.static_folder = 'static'
    loggy = logging.getLogger(__name__)
    loggy.addHandler(default_handler)
    loggy.setLevel(logging.DEBUG)

    formatter = RequestFormatter(
    '[%(asctime)s] %(remote_addr)s requested %(url)s\n'
    '%(levelname)s in %(module)s: %(message)s'
    )
    default_handler.setFormatter(formatter)

    # Register blueprints
    from app.views.main import main_bp
    from app.views.main import api_bp

    app.register_blueprint(main_bp, url_prefix='/')
    app.register_blueprint(api_bp, url_prefix='/api')

    return app, loggy
