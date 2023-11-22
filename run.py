# run.py
from app import create_app

app, log = create_app()

if __name__ == '__main__':
    app.run(debug=True)