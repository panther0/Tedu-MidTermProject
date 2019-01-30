import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

# 认证蓝图
bp = Blueprint('auth', __name__, url_prefix='/auth')

# 当用访问 /auth/register URL 时， 
# register 视图会返回用于填写注册 内容的表单的 HTML 。
# 当用户提交表单时，视图会验证表单内容，
# 然后要么再次显示表单并显示一个出错信息，
# 要么创建新用户并显示登录页面。
# 这里是视图代码

# @bp.route 关联了 URL /register 和 register 视图函数。
# 当 Flask 收到一个指向 /auth/register 的请求时
# 就会调用 register 视图并把其返回值作为响应。
@bp.route('/register', methods=('GET', 'POST'))
def register():
    # 如果用户提交了表单，那么 request.method 将会是 'POST' 。
    # 这咱情况下 会开始验证用户的输入内容。
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'

        # 以相同的方式哈希提交的 密码并安全的比较哈希值。
        # 如果匹配成功，那么密码就是正确的。
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            # session 是一个 dict ，它用于储存横跨请求的值。
            # 当验证 成功后，用户的 id 被储存于一个新的会话中。
            # 会话数据被储存到一个 向浏览器发送的 cookie 中，在后继请求中，浏览器会返回它。 
            # Flask 会安全对数据进行 签名 以防数据被篡改。
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')

# 注册一个 在视图函数之前运行的函数，不论其 URL 是什么。 
# load_logged_in_user 检查用户 id 是否已经储存在 session 中，
# 并从数据库中获取用户数据，然后储存在 g.user 中。 g.user 的持续时间比请求要长。 
# 如果没有用户 id ，或者 id 不存在，那么 g.user 将会是 None 。
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

# 注销的时候需要把用户 id 从 session 中移除。 
# 然后 load_logged_in_user 就不会在后继请求中载入用户了。
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# 装饰器返回一个新的视图，该视图包含了传递给装饰器的原视图。
# 新的函数检查用户 是否已载入。
# 如果已载入，那么就继续正常执行原视图，否则就重定向到登录页面。 
# 我们会在博客视图中使用这个装饰器。

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view