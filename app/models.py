
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    
    #def __init__(self, *args, **kwargs):
    #    super(User, self).__init__(*args, **kwargs)
    def __init__(self, id: int, login: str, password: str):
        self.id = id
        self.login = login
        self. password = password    
    
    def __repr__(self):
        return '<User id: {}, login: {}, password: {}>'.format(self.id, self.login, self.password)