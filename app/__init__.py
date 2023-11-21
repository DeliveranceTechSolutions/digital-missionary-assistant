# app/__init__.py
from flask import Flask, logging

def create_app():
    app = Flask(__name__)
    app.static_folder = 'static'

    # Register blueprints
    from app.views.main import main_bp
    from app.views.main import api_bp

    app.register_blueprint(main_bp, url_prefix='/')
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
