from app import db, manager
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, id, login, password):
        self.id = id
        self.login = login
        self.password = password


@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
