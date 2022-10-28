from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['APP_KEY'] = 'fdsfadfsadfasdf'

    return app