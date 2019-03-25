"""
只处理与主题相关的路由和视图
"""
import os
import pymysql
from flask import render_template, session, request, redirect
from . import test
from .. models import *
from .. import db
import datetime
from . import mathjx
import re

@test.route('/01-file', methods=['POST', 'GET'])
def file_views():
    if request.method == 'GET':
        return render_template("界面.html")
    else:
        # 1.从缓存区获取名称为picture的文件
        if 'files' in request.files:
            f = request.files['files']


            #2.将获取的文件使用其原始名称保存到static目录中
            # 2.1 获取文件名

            ftime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            ext = f.filename.split('.')[-1]
            filename = ftime + '.' + ext
            print("上传的文件名为:" + f.filename)
            # 2.2 将文件保存至static目录中
            # basedir = os.path.dirname(__file__)
            basedir = os.path.dirname(os.path.dirname(__file__))
            upload_path = os.path.join(basedir, 'static')
            mathjx.test_questions(upload_path)
        uname = request.form['uname']
        print('用户名称:' + uname)
        return "文件上传成功"


@test.route('/02-zxct', methods=['POST', 'GET'])
def zxct():
    if request.method == 'GET':
        courses = Course.query.all()
        return render_template('02-zxct.html',courses=courses)
    else:
        course = request.form['zxct']
        timu = request.form['timu']
        A = request.form['A']
        B = request.form['B']
        C = request.form['C']
        D = request.form['D']
        answer = request.form['answer']

        test = Test()
        test.course = course
        test.timu = timu
        test.A = A
        test.B = B
        test.C = C
        test.D = D
        test.answer = answer

        db.session.add(test)
        return redirect("02-zxct")


@test.route('/03-test/<course>', methods=['POST', 'GET'])
def test_views(course):
    if request.method == 'GET':
        tests = db.session.query(Test).filter(Test.course == course).limit(10).all()
        return render_template('03-test.html', tests=tests,course=course)
    else:
        tests = db.session.query(Test).filter(Test.course == course).limit(10).all()
        # l>数据库里的答案
        l = []
        # L>学生写的答案
        L = []
        for test in tests:
            a = re.findall('A|B|C|D', test.answer)
            l.append(a[0])
            id = str(test.id)
            L.append(request.form[id])
        # te = request.form

        # print(request.form)

        score = 0

        for j in range(10):
            print(l[j], end=" ")
            print(L[j], end=" ")
            if l[j] == L[j]:
                score += 10

        print(score)

    return "考试结束"





