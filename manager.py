from flask_script import Manager
from . import create_app, db
from flask_migrate import Migrate, MigrateCommand

app = create_app()
manager = Manager(app)
# 创建Migrate对象,并指定关联的app和db
migrate = Migrate(app, db)
# 为manager增加命令,允许做数据库的迁移操作
# 为manager绑定一个叫 db 的子命令,该子命令执行操作由MigrateCommand来提供
manager.add_command('db', MigrateCommand)


# # 创建数据库
@manager.command
def create_db():
    db.create_all()

# # 删除数据库
# @manager.command
# def drop_db():
#     db.drop_all()    


if __name__ == "__main__":
    manager.run()
