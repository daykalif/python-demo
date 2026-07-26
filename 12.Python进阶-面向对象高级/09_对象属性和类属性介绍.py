"""
案例: 演示对象属性 和 类属性.

属性介绍:
概述:
    它是1个名词, 用来描述事物的外在特征的.
分类:
    对象属性: 属于每个对象的, 即: 每个对象的属性值可能都不同. 修改A对象的属性, 不影响对象B
    类属性:   属于类的, 即: 能被该类下所有的对象所共享. A对象修改类属性, B对象访问的是修改后的.

对象属性:
    定义到 __init__ 魔法方法中的属性, 每个对象都有自己的内容.
    只能通过 对象名. 的方式调用.

类属性:
    定义到类中, 函数外的属性(变量), 能被该类下所有的对象所共享.
    既能通过 类名. 还能通过 对象名. 的方式来调用, 推荐使用 类名. 的方式.
"""


# 需求: 演示 对象属性 和 类属性相关.
# 1. 定义1个 Student类, 每个学生都有自己的 姓名, 年龄
class Student:
    # 2. 定义类属性
    teacher_name = '水镜先生'

    # 3. 定义对象属性，即：写到 __init__ 魔法方法中的属性.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 4. 定义__str__魔法方法，输出对象的信息.
    def __str__(self):
        return '姓名：%s，年龄：%d' % (self.name, self.age)


# 5. 测试
if __name__ == '__main__':
    # 场景一：对象属性
    s1 = Student(name='曹操', age=38)
    s2 = Student(name='曹操', age=38)

    # 修改s1的属性值
    s1.name = '刘备'
    s1.age = 48

    print(f's1: {s1}')
    print(f's2: {s2}')
    print('-' * 30)

    # 场景二：类属性
    # 1. 类属性可以通过 类名. 还可以通过 对象名. 的方式调用.
    print(s1.teacher_name)  # 水镜先生
    print(s2.teacher_name)  # 水镜先生
    print(Student.teacher_name)  # 水镜先生
    print('-' * 23)

    # 2.尝试用 对象名. 的方式来修改 类属性
    s1.teacher_name = '夯哥'  # 只能给s1对象赋值，不能给类属性赋值
    print(s1.teacher_name)  # 夯哥
    print(s2.teacher_name)  # 水镜先生
    print(Student.teacher_name)  # 水镜先生
    print('-' * 23)

    # 3. 如果要修改类变量的值，只能通过 类名. 的方式实现
    Student.teacher_name = 'Daykalif'
    print(s1.teacher_name)  # 夯哥
    print(s2.teacher_name)  # Daykalif
    print(Student.teacher_name)  # Daykalif
