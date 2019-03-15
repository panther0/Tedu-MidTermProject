# from flask_sqlalchemy import SQLAlchemy
from . import db


# db = SQLAlchemy()

class User(db.Model):
    # TODO: fileds here
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),unique=True)
    password = db.Column(db.String(256),nullable=False)
    email = db.Column(db.String(80))

    def __repr__(self):
        return 'User {0}'.format(self.username)
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, nullable=False)
    created = db.Column(db.TIMESTAMP(True), nullable=False)
    title = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)


