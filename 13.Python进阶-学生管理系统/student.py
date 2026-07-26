"""
该文件用于记录 学生类，学生的属性信息为：姓名，性别，年龄，手机号，描述信息
"""


# 1.定义学生类：
class Student:
    # 2.定义魔法方法，初始化属性信息
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

    # 3.定义魔法方法，用于打印学生信息
    def __str__(self):
        return f"学生姓名：{self.name}, 性别：{self.gender}, 年龄：{self.age}, 手机号：{self.phone}, 描述信息：{self.desc}"


# 4.测试
if __name__ == '__main__':
    # 4.1 创建学生对象
    student1 = Student('乔峰', '男', 38, '12345678901', '丐帮帮主')
    # 4.2 打印学生信息
    print(student1)
