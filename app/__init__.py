# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.static_folder = 'static'

    # Register blueprints
    from app.views.main import main_bp
    app.register_blueprint(main_bp, url_prefix='/')

    return app
