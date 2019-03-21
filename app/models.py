# from flask_sqlalchemy import SQLAlchemy
from . import db
from sqlalchemy import Column, Integer, String, DateTime, Boolean, TIMESTAMP, func


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),unique=True)
    password = db.Column(db.String(256),nullable=False)
    email = db.Column(db.String(80))
    utype = db.Column(db.String(20), nullable=False, default="user")
    isActive = db.Column(db.Boolean, nullable=False, default=True)

    posts = db.relationship("Post", backref='user', lazy="dynamic")

    def __repr__(self):
        return 'User {0}'.format(self.username)
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created = db.Column(db.TIMESTAMP(True), nullable=False, default=func.now())
    title = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)

        


