from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# pip install flask-migrate
# MigrateComman：执行迁移的命令
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)
app.secret_key = "dshfkaj"

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@127.0.0.1:3306/migratetest"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 使用迁移类将应用和数据库链接对象保存起来
Migrate(app, db)
# 创建终端命令的对象
manager = Manager(app)
# 将数据库的迁移命令添加到manager中
manager.add_command('aaa', MigrateCommand)


class Role(db.Model):
    # 定义表名
    __tablename__ = 'roles'
    # 定义对象
    id = db.Column(db.Integer, primary_key=True)
    nick_name = db.Column(db.String(64), unique=True)
    # 标题
    title = db.Column(db.String(64))
    # 高度
    height = db.Column(db.Integer)

    us = db.relationship('User', backref='role')

    # repr()方法显示一个可读字符串
    def __repr__(self):
        return 'Role:%s' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    manager.run()

# python demo1_migrate.py aaa init
# python demo1_migrate.py aaa migrate -m'initial'
# python demo1_migrate.py aaa upgrade

# 这里的aaa默认写成db
# manager.add_command('db', MigrateCommand)

# 总结迁移的命令：
# 1.迁移初始化（生成迁移所需文件夹migrations） python xxx.py db init
# 2.生成迁移版本文件 python xxx.py db migrate -m "注释"
# 3.执行迁移（往上迁移） python xxx.py db upgrade
#   执行迁移（往下迁移） python xxx.py db downgrade
# 4.回到指定版本  python xxx.py db downgrade 71b11e8c17fa