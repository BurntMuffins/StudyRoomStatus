from flask import Flask

#function to create a Flask application
def create_app():
    app = Flask(__name__)
    #app's secret key
    app.config['SECRET_KEY'] = "erxtcbhnjihgv"
    return app