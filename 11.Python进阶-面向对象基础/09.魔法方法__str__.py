"""
案例：演示 str魔法方法的 用法。

魔法方法：
概述/特点:
    Python内置的函数，在满足特定的场景下，会被 自动调用。
常用的魔法方法：
__init__()    在(每次)创建对象的时候，会自动触发该类的 __init__()函数。
__str__()     当用print()函数 打印对象的时候，会自动调用该对象(所在类)的 str魔法方法。
              该魔法方法默认打印的是对象的地址值，无意义，一般都会重写，改为打印 对象的各个属性值。
__del__()
"""


# 1. 定义汽车类.
class Car:
    def __init__(self, color, number):
        """
        该魔法方法用于给 汽车类 对象的属性 赋值。
        :param color: 车的颜色
        :param number: 车的轮胎数
        """
        self.color = color
        self.number = number

    # 魔法方法str()，默认打印地址值，无意义，一般会重写，改为打印对象的各个属性值。
    def __str__(self):
        return f'颜色: {self.color}, 轮胎数: {self.number}'


# 3.创建该类的对象。
c1 = Car(color='绿色', number=4)
print(c1)  # 输出语句打印对象，默认调用了该对象 所在类的 str魔法方法。
print('-' * 23)

c2 = Car(color='红色', number=6)
print(c2)
