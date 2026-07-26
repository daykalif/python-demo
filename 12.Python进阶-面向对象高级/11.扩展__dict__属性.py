"""
案例: 演示Python内置的__dict__属性.

__dict__ 属性介绍:
它是Python内置的属性，可以把对象转成字典形式.


小结：
1. 对象.__dict__ 属性可以把对象转成字典形式.
2. 对象(**字典）可以将字典转成对象.
"""


class Student:
    # 定义魔法方法，初始化属性信息
    def __init__(self, name, gender, age, phone, desc):
        """
        该魔法方法，用于初始化 属性信息
        :param name:    学生姓名
        :param gender:  性别
        :param age:     年龄
        :param phone:   手机号
        :param desc:    描述信息
        """
        self.name = name
        self.gender = gender
        self.age = age
        self.phone = phone
        self.desc = desc

    # 定义魔法方法，用于打印学生信息
    def __str__(self):
        return f"学生姓名：{self.name}, 性别：{self.gender}, 年龄：{self.age}, 手机号：{self.phone}, 描述信息：{self.desc}"


# 需求1: 把 学生对象 → 字典形式，属性名做键，属性值做值.
s1 = Student(name='德桦', gender='男', age=81, phone='111', desc='刻骨铭心')
print(s1)  # 学生姓名：德桦, 性别：男, 年龄：81, 手机号：111, 描述信息：刻骨铭心
print(type(s1))  # <class '__main__.Student'>

my_dict = s1.__dict__
print(my_dict)  # {'name': '德桦', 'gender': '男', 'age': 81, 'phone': '111', 'desc': '刻骨铭心'}
print(type(my_dict))  # <class 'dict'>

print('-' * 23)

# 需求2: 把 [学生对象, 学生对象, 学生对象] → [字典, 字典, 字典]
s1 = Student(name='德桦', gender='男', age=81, phone='111', desc='刻骨铭心')
s2 = Student(name='志奇', gender='男', age=22, phone='222', desc='我不是紫琦')
s3 = Student(name='紫琦', gender='男', age=66, phone='333', desc='有请志奇')

stu_list = [s1, s2, s3]

# [<__main__.Student object at 0x13aeb3290>, <__main__.Student object at 0x13aeb3260>, <__main__.Student object at 0x13aeb3350>]
print(stu_list)

# 列表推导式
stu_list = [stu.__dict__ for stu in stu_list]
# [{'name': '德桦', 'gender': '男', 'age': 81, 'phone': '111', 'desc': '刻骨铭心'}, {'name': '志奇', 'gender': '男', 'age': 22, 'phone': '222', 'desc': '我不是紫琦'}, {'name': '紫琦', 'gender': '男', 'age': 66, 'ph': '有请志奇'}]
print(stu_list)

print('-' * 23)

# 需求3: 把 {'name': '德桦', 'gender': '男', 'age': 81, 'phone': '1111', 'desc': '刻骨铭心'} → 学生对象
my_dict = {'name': '德桦', 'gender': '男', 'age': 81, 'phone': '1111', 'desc': '刻骨铭心'}

# 不推荐该方式
s5 = Student(my_dict['name'], my_dict['gender'], my_dict['age'], my_dict['phone'], my_dict['desc'])
print(s5)
print(type(s5))

print('-' * 23)

# 推荐方式
s6 = Student(**my_dict)
print(s6)
print(type(s6))
