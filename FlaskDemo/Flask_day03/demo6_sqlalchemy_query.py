# 数据库通过ORM连接使用：

from flask import Flask

# 安装flask-sqlalchemy
# pip install flask-sqlalchemy

# pip install PyMySQL

# 如果连接的是mysql数据库，需要安装mysqldb
# pip install flask-mysqldb

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 指定使用的数据库的链接地址
# mysql://root:root@127.0.0.1:3306/test_27
# mysql:数据库类型； 第一个root:我的数据库用户名  第二个root:我的数据库密码；   127.0.0.1:3306: 地址和端口   test_27:创建的数据库名称
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@127.0.0.1:3306/test_27"
# 是否追踪数据库的修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化:创建一个SQLAlchemy对象,需要放在config后面
db = SQLAlchemy(app)


# 命令后运行：mysql -u root -p
# 输入密码时直接回车
# 创建数据库 create database test_27 charset utf8;    (注意：一定要有分号)
# 查看数据库show databases;
# 使用数据库  use test_27
# 查看表格   show tables;
# 排序表格  desc roles;
# 查看表格中数据  select * from roles;


# 定义数据库表（如不指定表名，默认以类名小写当作表名，此处默认为role当作表名）
# 一个角色可以对应多个用户
# 角色  1的一方
class Role(db.Model):
    # 指定该模型对应数据库中的表名，如果不指定为类名小写
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # backref在这行代码的作用是：给前面的User添加一个属性，名字叫backref的值
    # 以便可以直接通过user.role方法一的一方的数据
    users = db.relationship('User', backref='role')

    # 显示当前对象的描述字符串，可以自己定义
    def __repr__(self):
        return 'Role %d %s' % (self.id, self.name)


# 用户 多的一方
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    # 添加外键记录一的一方的主键id，为了能够直接查询出一的一方的数据
    role_id = db.Column(db.Integer, db.ForeignKey(Role.id))

    # 显示当前对象的描述字符串，可以自己定义
    def __repr__(self):
        return 'User %d %s' % (self.id, self.name)


@app.route('/')
def index():
    return 'Hello World!'


if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    ro1 = Role(name='admin')
    ro2 = Role(name='user')
    # db.session.add(ro1)
    # db.session.add(ro2)
    db.session.add_all([ro1, ro2])
    db.session.commit()

    user1 = User(name='laowang', role_id=ro1.id)
    user2 = User(name='laoli', role_id=ro1.id)
    user3 = User(name='laozhang', role_id=ro2.id)
    db.session.add_all([user1, user2, user3])
    db.session.commit()

    app.run(debug=True)

"""

进入当前目录，ipython
输入： from demo6_sqlalchemy import *
查看表格中数据:  select * from roles   此时为空
创建用户名：role = Role(name='admin')
此时，id的值为空：role.id  
添加数据库的session：  db.session.add(role)  
                    db.session.commit() 

查看表格中数据  select * from roles，此时里面有数据
此时，id的值为空：role.id 打印值为 1 

修改信息：role.name = 'laowang' 
提交修改： db.session.commit() 

删除数据：db.session.delete(role)  
提交修改： db.session.commit() 

Role.query.all()
User.query.all()
User.query.get(1)

user = User.query.get(3)  
user.role_id    -->打印输出：2
Role.query.get(user.role_id)

role = Role.query.get(1) 
role.users
"""


"""
查询所有用户数据
    User.query.all()
查询有多少个用户
    User.query.count()
查询第一个用户
    User.query.first()
查询id为4的用户【3种方式】
    User.query.get(4)
    User.query.filter_by(id=4).first()
    User.query.filter(User.id == 4).first()
查询名字【结尾/开始/包含】字符为g的所有数据
    User.query.filter(User.name.endwith('g')).all()    
    User.query.filter(User.name.startwith('g')).all()    
    User.query.filter(User.name.contains('g')).all()    
查询名字不等于wang的所有数据【2种方式】
    User.query.filter(not_(User.name == 'wang')).all()
    User.query.filter(User.name != 'wang').all()
查询名字和邮箱都以li开头的所有数据【2种方式】
    User.query.filter(User.name.startwith('li'),User.email.startwith('li')).all()
    User.query.filter(and_(User.name.startwith('li'),User.email.startwith('li'))).all()
查询password是'123456' 或者 email以'itheima.com'结尾的数据
    User.query.filter(or_(User.password == '123456' || User.email.startwith('itheima.com'))).all()
查询id为[1,3,5,7,9]的用户列表
    User.query.filter(User.id.in_([1,3,5,7,9])).all()
查询name为liu的角色数据
    User.query.filter(User.username == 'liu').first().role
查询所有用户的数据，并以邮箱排序
    User.query.order_by(User.email).all()       #等同于User.query.order_by(User.email.asc()).all()
    User.query.order_by(User.email.desc()).all()
查询第二页的数据,每页3个
    paginate = User.query.paginate(2,3)
    当前页数据：
    paginate.items
    总页数：
    paginate.pages
    当前页码：
    paginate.page
"""