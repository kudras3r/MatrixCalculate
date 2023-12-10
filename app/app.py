
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

from calculate.blueprint import calc


app = Flask(__name__)
app.config.from_object(Config)


db = SQLAlchemy(app)
app.app_context().push()


app.register_blueprint(calc, url_prefix='/calc')