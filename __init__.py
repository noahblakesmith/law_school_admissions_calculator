from flask import Flask

from .routes import routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)