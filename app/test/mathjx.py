import pymysql 
from sys import argv
from .. import db
from .. models import Test

# db = pymysql.connect('localhost','root','123456','test')                    

def inserts(L):
    test = Test()
    test.course = L[0]
    test.timu = L[1]
    test.A = L[2]
    test.B = L[3]
    test.C = L[4]
    test.D = L[5]
    test.answer = L[6]
    
    # cursor = db.cursor()
     #插入用户
    # sql = '''insert into test(course,timu,A,B,C,D,answer)
    #     values('%s','%s','%s','%s','%s','%s','%s')
    # '''%(course,timu,A,B,C,D,answer)
    # print(course)
    # print(timu)
    # print(A)
    # print(B)
    # print(C)
    # print(D)
    # print(answer)

    # try:
    #     cursor.execute(sql)
    #     db.commit()
    # except Exception:
    #     db.rollback()
    db.session.add(test)    

def test_questions(f):
    try:
        f = open(f)
        for line in f:
            L = line.split(',')
            # print(L[0],L[1],L[2],L[3],L[4],L[5],L[6])
            inserts(L)
          
    except Exception as e:
        print("打开文件失败",e)


if __name__ == "__main__":
    test_questions(f)


