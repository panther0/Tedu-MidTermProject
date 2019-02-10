from flask import Flask,url_for,request,render_template
# app = Flask(__name__)
from __init__ import create_app
# from sailings import config

app = create_app()


@app.route('/runhello')
def runhello():
    return 'Hello, World! - from run.py'

@app.route('/')
def runindex():
    index_page = """
<html>
<head>
  <title>Hello</title>
  <style>
    h1 {
      color: #333333;
      font-size: 48px;
      text-shadow: 3px 3px 3px #666666;
    }
  </style>
</head>
<body>
  <h1>Hello, world! - from run.py</h1>
</body>
</html>"""
    return index_page



@app.route('/hello')
def index():
    return render_template("./template/hello.html",error=error)

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
        return 'login_POST'
    else:
        return 'login_GET'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

if __name__ == "__main__":
    app.run(host='127.0.0.1',debug=True)