"""
案例：演示多态入门.

多态概述：
    专业版：同一个函数，接收不同的参数，有不同的效果
    大白话：同一个事物在不同时刻表现出来的不同状态，形态。

前提条件：【python语法中，多态虽然名义上要满足以下条件，但是如果都不满足，python也不会报错；java不满足下面条件就会报错】
    1. 要有继承。
    2. 要有方法重写，不然多态无意义。
    3. 要有父类引用指向子类对象。

案例：
    动物类案例.
"""


# 1.定义动物类
class Animal:  # 抽象类(也叫：接口)
    def speak(self):  # 抽象方法
        pass


# 2. 定义子类，狗类.
class Dog(Animal):
    def speak(self):
        print('狗叫：汪汪汪')


# 3. 定义子类，猫类.
class Cat(Animal):
    def speak(self):
        print('猫叫：喵喵喵')


# 汽车类（python中虽然没有继承Animal，但是多态还是会执行）
class Car:
    def speak(self):
        print('车叫：滴滴滴')


# 4. 定义函数，接收不同的动物对象，调用speak方法
def make_noise(an: Animal):  # an:Animal = Dog()
    an.speak()


# 5. 测试.
if __name__ == '__main__':
    an: Animal = Dog()  # 父类引用指向子类对象
    d: Dog = Dog()  # 创建狗类对象

    # 5.1 创建狗类，猫类对象.
    d = Dog()
    c = Cat()
    e = Car()

    # 5.2 演示多态.
    make_noise(d)
    make_noise(c)
    make_noise(e)
