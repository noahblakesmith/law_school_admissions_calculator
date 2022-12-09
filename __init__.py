from flask import Flask
app = Flask(__name__)


# this is the "web_app/__init__.py" file...

#import os
#from dotenv import load_dotenv
from flask import Flask

import app.route



def create_app():
    app = Flask(__name__)
    #app.config["SECRET_KEY"] = SECRET_KEY

    app.register_blueprint(home_routes)
    app.register_blueprint(stocks_routes)
    #app.register_blueprint(book_routes)
    #app.register_blueprint(weather_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)