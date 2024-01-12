"""

    Created, supported, updated by kudraser
    
    Contacts
    tg: https://t.me/kudras3r_dev
    GitHub: https://github.com/kudras3r
    vk: https://vk.com/dgcihf

"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

manager = LoginManager(app)

db = SQLAlchemy(app)
db.create_all()

app.app_context().push()
