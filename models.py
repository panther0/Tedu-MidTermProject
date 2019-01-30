from app import db #db是在flaskr/__init__.py生成的关联后的SQLAlchemy实例

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(320), unique=True)
    password = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Admin(db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(320), unique=True)
    password = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


if __name__ == '__main__':
    db.create_all() 
#  admin_role =Role(name = 'Admin') #实例化
#  mod_role = Role(name = 'Moderator')
#  user_role =Role(name = 'User')
#  user_john = User(username = 'john',role=admin_role)#role属性也可使用，虽然他不是真正的数据库列，但却是一对多关系的高级表示
#  user_susan = User(username = 'susan',role= user_role)
#  user_david = User(username = 'david',role = user_role)
#  db.session.add_all([admin_role,mod_role,user_role,user_john,user_susan,user_david])  # 准备把对象写入数据库之前，先要将其添加到会话中，数据库会话db.session和Flask session对象没有关系，数据库会话也称事物
#  db.session.commit()#提交会话到数据库