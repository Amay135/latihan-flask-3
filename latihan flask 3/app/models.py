from . import db

class User(db.Model):
    id = db.Coloumn(db.Integer, primary_key=True)
    username = db.Coloumn(db.string(150), unique=True, nullable=False)
    password = db.Coloumn(db.string(150), nullable=False)