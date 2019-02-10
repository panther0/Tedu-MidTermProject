import os
from flask import Flask
from flask import url_for, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
# from app import models,views
# from sailings import run


# db = SQLAlchemy()
# 生成一个可以操作app数据库的SQLAlchemy实例db
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # SECRET_KEY 是被 Flask 和扩展用于保证数据安全的。在开发过程中， 为了方便可以设置为 'dev' ，但是在发布的时候应当使用一个随机值来 重载它
        SECRET_KEY='dev',
        # DATABASE MYSQL 数据库文件存放在路径。它位于 Flask 用于存放实例的 app.instance_path 之内。
        DATABASE=os.path.join(app.instance_path, 'sailings.sqlite'),
        # 其格式为：mysql://username:password@server/db？编码
        # 注意默认使用mysqldb连接数据库，要使用pymysql就需要用mysql+pymysql的格式；
        # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/sailingsDB?charset=utf8'
        # 设置是否在每次连接结束后自动提交数据库中的变动。
        # SQLALCHEMY_COMMIT_ON_TEARDOWN = True

        # 下面两项调试阶段启动，部署时关闭
        # SQLALCHEMY_TRACK_MODIFICATIONS = True
        # SQLALCHEMY_ECHO = True
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
        # app.config.from_pyfile() 使用 config.py 中的值来重载缺省配置，如果 config.py 存在的话。 例如，当正式部署的时候，用于设置一个正式的 SECRET_KEY 。
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
        # test_config 也会被传递给工厂，并且会替代实例配置。这样可以实现 测试和开发的配置分离，相互独立。

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
        # os.makedirs() 可以确保 app.instance_path 存在。 Flask 不会自动 创建实例文件夹，但是必须确保创建这个文件夹，因为 SQLite 数据库文件会被 保存在里面。
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/inithello')
    def hello():
        return 'Hello, World! - from init'
 
    # 导入并注册 蓝图。
 
    # 这个函数其读取app的配置参数，将和数据库相关的配置加载到SQLAlchemy对象中
    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)

    from . import index
    app.register_blueprint(index.bp)
    app.add_url_rule('/', endpoint='index')
    
    return app