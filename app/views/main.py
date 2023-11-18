from flask import render_template, Blueprint

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html', title='Home')

@main_bp.route('/about')
def about():
    return render_template('about.html', title='About Us')

# Add more routes as needed
