from flask import (
    Blueprint, render_template, url_for, request
)
from sailings.db import get_db


# 认证蓝图
bp = Blueprint('exam',__name__,url_prefix='/exam')


@bp.route('/exam')
def exam():
    """Show all the posts, most recent first."""
    db = get_db()
    posts = db.execute(
        'SELECT e.id, question, opt1, opt2, opt3, opt4'
        ' FROM exam e JOIN user u ON e.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('exam/exam.html', posts=posts)



@bp.route('setqst',methods=('GET','POST'))
def setqst():
    if request.method == 'POST':
        pass

    return render_template('exam/setqst.html')