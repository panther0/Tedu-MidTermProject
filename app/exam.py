from flask import (
    Blueprint, render_template, url_for, request, g, session
)
from . import db
from .models import *
import re


# from .models import Exam

# 认证蓝图
bp = Blueprint('exam',__name__,url_prefix='/exam')


@bp.route('/exam', methods=['GET', 'POST'])
def exam():
    # # TODO: 地址栏传入course
    course = request.args.get("course")
    if request.method == 'POST':
    #     # tests = db.session.query(Test).filter(Test.course == course).limit(10).all()
    #     # l>数据库里的答案
    #     l = []
    #     # L>学生写的答案
    #     L = []
    #     for test in g.tests:
    #         # a = re.findall('A|B|C|D', test.answer)
    #         l.append(test.answer)
    #         # l.append(a[0])
    #         id = str(test.id)
    #         L.append(request.form[id])
    #     score = 0

    #     for j in range(10):
    #         # print(l[j], end=" ")
    #         # print(L[j], end=" ")
    #         if l[j] == L[j]:
    #             score += 10
        score = 0
        list = request.form
            
        for t in list:
            # print(t)
            # print(list[t])
            # idstr = str(t)
            ans = db.session.query(Test).filter_by(id=t).one().answer
            if list[t] == ans:
                score += 10
        print(score)

        # TODO:JiaJUN:结果导入数据库及结果查询
        return ("考试结束,您获得了%d分"%score)
    tests = db.session.query(Test).filter(Test.course == course).order_by(func.random()).limit(10).all()
    # g.tests = tests
    # session.tests = tests
    # g.course = course
    return render_template('exam/exam.html', tests=tests,course=course)


@bp.route('setqst',methods=('GET','POST'))
def setqst():
    if request.method == 'POST':
        pass

    return render_template('exam/setqst.html')


@bp.route('zxct',methods=('GET','POST'))
def zxct():
    courses = db.session.query(Course).all()
    if request.method == 'POST':
        list = request.form
        test = Test()
        test.course = list["course"]
        test.timu = list["timu"]
        test.A = list["A"]
        test.B = list["B"]
        test.C = list["C"]
        test.D = list["D"]
        test.answer = list["answer"]
        db.session.add(test)

    return render_template('exam/zxct.html',courses=courses)