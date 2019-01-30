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


git stash test (储藏)
add James
add James
add James