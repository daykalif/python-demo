"""
案例：演示魔法方法之 init 有参版，实际开发常用。

回顾:
__init__()魔法方法，在创建对象的时候，会被自动调用，一般用于给该类对象 的属性进行初始化。

大白话举例:
    无参版 init →  默认上的有底色，你需要重新涂色(覆盖底色)
    有多参 init →  默认没有涂色的石膏娃娃，我们根据喜好自由涂色即可。
"""


# 需求：创建汽车类，不给默认值，由汽车对象 外部各自赋值即可。
# 1. 定义汽车类.
class Car:
    # 2.有参的 __init__()函数，参数值由：外部对象自行赋值.
    def __init__(self, color, number):
        """
        该魔法方法用于给 汽车类 对象的属性 赋值。
        :param color: 车的颜色
        :param number: 车的轮胎数
        """
        self.color = color
        self.number = number

    #  定义show()函数，打印该类对象的 各个属性值。
    def show(self):
        print(f'颜色: {self.color}, 轮胎数: {self.number}')


# 3. 创建汽车类对象.
# c = Car()  报错，因为默认调用了init()函数，但是该函数有参数，则必须传参.
c1 = Car("red", 4)
c1.show()

print('-' * 34)

c2 = Car("green", 6)
c2.show()
