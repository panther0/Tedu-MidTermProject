# from flask_sqlalchemy import SQLAlchemy
from . import db
from sqlalchemy import Column, Integer, String, DateTime, Boolean, TIMESTAMP, func, Enum
import enum

# 用户
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),unique=True)
    password = db.Column(db.String(256),nullable=False)
    # 性别
    class GdEnum(enum.Enum):
        M = "M"
        F = "F"
    gender = db.Column(db.Enum(GdEnum), default=GdEnum.M)
    email = db.Column(db.String(80))
    isActive = db.Column(db.Boolean , nullable=False, default=True)

    posts = db.relationship("Post", backref='user', lazy="dynamic")
    # 用户类别：user/teacher/student/admin
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"))

    def __repr__(self):
        return 'User {0}'.format(self.username)

# 用户角色
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rname = db.Column(db.String(20), nullable=False)
    user = db.relationship('User',backref='role', lazy='dynamic')

    def __repr__(self):
        return 'Role-{0}'.format(self.rname)


# 博客    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.TIMESTAMP(True), nullable=False, default=func.now())
    title = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# 考试题        
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

# 考试名
class Course(db.Model):
    __tablename__="course"
    id = db.Column(db.Integer, primary_key=True)
    # cid = db.Column(db.String(128))
    cname = db.Column(db.String(200),nullable=False)
    # student = db.Column(db.String(256),db.ForeignKey(Student.sid))
    user = db.relationship("User",backref="course",lazy="dynamic")

    def __repr__(self):
        return 'Course-{0}'.format(self.cname)

# 分数
class Score(db.Model):
    __tablename__="score"
    id = db.Column(db.Integer,primary_key = True,autoincrement=True)
    # sid = db.Column(db.String(200),nullable=False)
    cid = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Integer,nullable=False)


# 模型用于删除数据库错误的　Alembic Num
class Alembic(db.Model):
    __tablename__ = 'alembic_version'
    version_num = db.Column(db.String(32), primary_key=True, nullable=False)

    @staticmethod
    def clear_A():
        for a in Alembic.query.all():
            print (a.version_num)
            db.session.delete(a)
        db.session.commit()
        print ('======== data in Table: Alembic cleared!')
