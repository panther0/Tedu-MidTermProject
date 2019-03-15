from flask_sqlalchemy import SQLAlchemy
import click
from flask import current_app, g
# g 是一个特殊对象，独立于每一个请求。在处理请求过程中，它可以用于储存 可能多个函数都会用到的数据。
# 把连接储存于其中，可以多次使用，而不用在同一个 请求中每次调用 get_db 时都创建一个新的连接。
# from flask.cli import with_appcontext
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from . import db


# def get_db():
#     if 'db' not in g: 
#         # 建立一个数据库连接，该连接指向配置中的 DATABASE 指定的文件。
#         # 这个文件现在还没有建立，后面会在初始化数据库的时候建立该文件。
#         g.db = sqlite3.connect(
#             # current_app 是另一个特殊对象，该对象指向处理请求的 Flask 应用。
#             # 这里 使用了应用工厂，那么在其余的代码中就不会出现应用对象。
#             # 当应用创建后，在处理 一个请求时， get_db 会被调用。这样就需要使用 current_app 
#             current_app.config['DATABASE'], 
#             detect_types=sqlite3.PARSE_DECLTYPES
#         )
#         # 告诉连接返回类似于字典的行，这样可以通过列名称来操作 数据。
#         g.db.row_factory = sqlite3.Row

#     return g.db


# def init_db(app):
#     # 创建db
#     db = SQLAlchemy(app)
#     # 打开一个文件，该文件名是相对于 sailings 包的。这样就不需要考虑以后应用具体部署在哪个位置。 g
#     # et_db 返回一个数据库连接，用于执行文件中的命令。
#     with current_app.open_resource('schema.sql') as f:
#         db.executescript(f.read().decode('utf8'))

# # 定义一个名为 init-db 命令行，它调用 init_db 函数，并为用户显示一个成功的消息。
# @click.command('init-db')
# @with_appcontext
# def init_db_command():
#     """Clear the existing data and create new tables."""
#     init_db()
#     click.echo('Initialized the database.')



def init_app(app):
    db = SQLAlchemy(app)
    db.create_all()

# app.teardown_appcontext() 告诉 Flask 在返回响应后进行清理的时候调用此函数。

# app.cli.add_command() 添加一个新的 可以与 flask 一起工作的命令。

# 在工厂中导入并调用这个函数。在工厂函数中把新的代码放到 函数的尾部，返回应用代码的前面。
