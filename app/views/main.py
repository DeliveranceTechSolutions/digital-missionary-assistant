from flask import render_template, request, jsonify, Blueprint, current_app
from app.auth.login import login as key
import logging

################ VIEWS BLUEPRINT ################
main_bp = Blueprint('main', __name__)
api_bp = Blueprint('api', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html', title='Home')

@main_bp.route('/about')
def about():
    return render_template('about.html', title='About Us')

@main_bp.route('/login')
def auth():
    return render_template('login.html', title='Login')
# Add more routes as needed

############## API BLUEPRINT ################
@api_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if data is not None:
        # Fetch the login key
        res = key(data[0], data[1])

        # Process the JSON data
        result = {'message': f"{res}"}
        return jsonify(result), 200

    else:
        error_message = {'error': 'Invalid JSON data'}
        return jsonify(error_message), 400

    