关于添加远程库的说明：


第1步：创建SSH Key：

    在用户主目录下，看看有没有.ssh目录，
    如果有，再看看这个目录下有没有id_rsa和id_rsa.pub这两个文件，
    如果已经有了，可直接跳到下一步。
    如果没有，打开Shell（Windows下打开Git Bash），创建SSH Key：

    $ ssh-keygen -t rsa -C "youremail@example.com"
    "youremail@example.com"----请换成你自己的邮箱地址

第2步：找到 id_rsa.pub
    如果一切顺利的话，可以在用户主目录里找到.ssh目录，
    里面有id_rsa和id_rsa.pub两个文件，
    这两个就是SSH Key的秘钥对，id_rsa是私钥，不能泄露出去，
    id_rsa.pub是公钥，可以放心地告诉任何人。


第3步：添加远程库
    $ git remote add origin git@github.com:panther0/Tedu-MidTermProject.git



初始化数据库：
命令：
flask init-db
以下为返回
Initialized the database.


添加 Blueprint 步骤：
    1. 创建 Blueprint 
       bp = Blueprint('<Blueprint_name>', __name__, url_prefix='/<Blueprint_name>')
    2. 创建视图函数
    3. 使用 app.register_blueprint() 导入并注册 蓝图。
       新的代码放在工厂函数的尾部返回应用之前。
    4. 添加模板



Connect to AWS:
    $ ssh -i "sailingsEDU.pem" ec2-user@ec2-13-229-129-246.ap-southeast-1.compute.amazonaws.com

     
