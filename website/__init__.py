from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['APP_KEY'] = 'fdsfadfsadfasdf'
    app.secret_key = 'sdasdasdasdasd'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
