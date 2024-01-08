from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

manager = LoginManager(app)

db = SQLAlchemy(app)

app.app_context().push()

db.create_all()
