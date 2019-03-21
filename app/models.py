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
    course_id = db.Column(db.String(128), db.ForeignKey("course.cid"))

    def __repr__(self):
        return 'User {0}'.format(self.username)
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.TIMESTAMP(True), nullable=False, default=func.now())
    title = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

        

class Test(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(20),nullable=False)
    timu = db.Column(db.String(256),nullable=False)
    A = db.Column(db.String(256),nullable=False)
    B = db.Column(db.String(256),nullable=False)
    C = db.Column(db.String(256),nullable=False)
    D = db.Column(db.String(256),nullable=False)
    answer= db.Column(db.String(256),nullable=False)
    tihao = db.Column(db.Integer,nullable=True)


class Course(db.Model):
    __tablename__="course"
    id = db.Column(db.Integer, primary_key=True)
    cid = db.Column(db.String(128))
    cname = db.Column(db.String(200),nullable=False)
    # student = db.Column(db.String(256),db.ForeignKey(Student.sid))
    user = db.relationship("User",backref="course",lazy="dynamic")