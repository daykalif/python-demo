from flask import Flask
from flask_sqlalchemy import SQLAlchemy, models_committed

app = Flask(__name__)
app.secret_key = "dshfkaj"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@127.0.0.1:3306/manytomany"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# 创建一个单独的表
tb_Student_Course = db.Table(
    "student_course",
    db.Column('student_id', db.Integer, db.ForeignKey("student.id")),
    db.Column('course_id', db.Integer, db.ForeignKey("course.id"))
)


# 使用模型去表示一张表
class Student(db.Model):
    """学生表"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 当前学生选修了哪些课程
    courses = db.relationship('Course',
                              backref=db.backref("students", lazy="dynamic"),
                              lazy="dynamic",
                              # lazy="subquery",
                              secondary=tb_Student_Course)


# lazy="dynamic",
# 如果不指定该值，那么当student查询数据之后，course就已经有值（已经从Course表里面把数据查询出来了）
# 如果指定该值，那么当student查询数据之后，course并没有具体的值，而只是查询对象
# 如果只是查询对象，那么就可以在用的时候再去数据库查询，避免不必要的查询操作，影响性能
# 默认为lazy="subquery"
class Course(db.Model):
    """课程表"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)


# 运行安装blinker, pip install blinker
# 订阅谁发出的信号，当信号发出之后，会调用其装饰的函数
@models_committed.connect_via(app)
def db_changer(app, changes):
    print(changes)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    # 添加测试数据
    stu1 = Student(name='张三')
    stu2 = Student(name='李四')
    stu3 = Student(name='王五')

    cou1 = Course(name='物理')
    cou2 = Course(name='化学')
    cou3 = Course(name='生物')

    stu1.courses = [cou2, cou3]
    stu2.courses = [cou2]
    stu3.courses = [cou1, cou2, cou3]

    db.session.add_all([stu1, stu2, stu3])
    db.session.add_all([cou1, cou2, cou3])

    db.session.commit()

    app.run(debug=True)
