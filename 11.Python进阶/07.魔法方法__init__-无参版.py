"""
在Python中，有一些可以给Python类增加魔力的特殊方法，它们总是被双下划线所包围，我们称之为魔法方法。
在特殊情况下会被自动调用，不需要开发者手动去调用。

__魔法方法名__()
"""

"""
案例：演示 init魔法方法的 用法。

魔法方法：
概述/特点:
    Python内置的函数，在满足特定的场景下，会被 自动调用。
常用的魔法方法：
    __init__()    在创建对象的时候，会自动触发该类的 __init__()函数。
    __str__()
    __del__()
"""


class Car:
    # 1.1 在魔法方法 init()中，初始化：属性。
    def __init__(self):
        print('我是 无参 init 魔法方法')
        # 1.2 在init魔法方法中，初始化属性，则：该类所有的对象，一创建，就有这些属性了。
        self.color = '黑色'
        self.number = 3

    # 1.3 定义show()函数，打印该类对象的 各个属性值。
    def show(self):
        print(f'颜色: {self.color}, 轮胎数: {self.number}')


# 2. 创建汽车类对象.
c1 = Car()  # 会自动调用 __init__()函数.

# 修改c1的属性值
c1.color = '红色'
c1.number = 6

# 打印c1对象的属性值.
print(c1.color, c1.number)
c1.show()

print('-' * 34)
c2 = Car()
c2.show()
