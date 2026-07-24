"""
案例：演示多继承。

需求：小明是个爱学习的好孩子，想学习更多的摊煎饼果子技术，于是，在百度搜索到黑马程序员学校，报班来培训学习摊煎饼果子技术。

扩展：MRO机制。

解释：
    Python中有MRO机制，可以查看某个对象，在调用函数时的 顺序，即：先找哪个类，后找哪个类。

格式：
    类名.mro()
    类名.__mro__
"""


# 1. 定义师傅类.
class Master:
    # 1.1 定义师傅类属性.
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    # 1.2 定义师傅类方法.
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 2. 定义黑马学校类.
class School:
    # 2.1 定义学校类属性.
    def __init__(self):
        self.kongfu = '[黑马AI煎饼果子配方]'

    # 2.2 定义学校类方法.
    def make_cake(self):
        print(f'运用 {self.kongfu} 制作煎饼果子')


# 3.定义徒弟类 → 有个对象叫 小明.
class Prentice(School, Master):  # 继承默认是 从左往右，就近原则
    pass  # 但是可以通过 super() 来调用父类的方法，从而修改继承的默认方式


# 4.测试
xm = Prentice()
print(xm.kongfu)
xm.make_cake()
print("-" * 30)

# 5. 查看mro机制的结果.
print(Prentice.mro())  # Prentice → School → Master → object
print(Prentice.__mro__)  # Prentice → School → Master → object
