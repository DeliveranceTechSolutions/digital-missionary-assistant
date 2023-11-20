from flask import render_template, Blueprint

main_bp = Blueprint('main', __name__)

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
