"""
案例：创建类的格式介绍。

格式1：
    class 类名:
        pass

格式2：
    class 类名():
        pass

格式3：
    # class 类名(父类名):
    class 类名(object):
        pass
"""


# 需求：定义老师类
# class Teacher:
# class Teacher():

class Teacher(object):  # object是所有类的父类，Python中所有的类都直接或者间接继承自object类.
    pass


t1 = Teacher()
print(t1)   # <__main__.Teacher object at 0x105240bf0>
