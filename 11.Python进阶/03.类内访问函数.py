"""
案例：演示通过 self关键字实现 在类内访问其它函数。

self关键字：
概述：
    代表本类当前对象的引用，谁(哪个对象)调用，self就代表谁。
作用：
    用于实现函数 区分 不同对象的。

总结：
💡 1. 在 类外 访问类中的行为，需要通过 对象名. 的方式访问。
   2. 在 类内 访问类中的行为，需要通过 self. 的方式访问。
"""


# 需求：定义汽车类，类内有run()函数，并在work()中调用run()函数，创建该类对象，调用上述的函数


# 1. 定义汽车类
class Car:
    # 属性(名词)

    # 行为(动词)
    # 1.1 run()函数
    def run(self):
        print(f'{self} 汽车在跑...')

    # 1.2 work()函数，在其内部调用run()
    def work(self):
        print(f'我是work函数，我的self值：{self}')
        self.run()  # self = 本类当前对象的引用


# 2.在类外访问Car类的行为(函数)
c1 = Car()

# <__main__.Car object at 0x12830a5a0>
print(f'c1对象：{c1}')

# 4969244064
print(f'c1对象的地址值：{id(c1)}')

# <__main__.Car object at 0x12830a5a0> 汽车在跑...
c1.run()

print('-' * 34)

# 我是work函数，我的self值：<__main__.Car object at 0x12830a5a0>
# <__main__.Car object at 0x12830a5a0> 汽车在跑...
c1.work()

print('=' * 34)  # 分割线

# 3.再次创建对象
c2 = Car()

# c2对象：<__main__.Car object at 0x12830a5d0>
print(f'c2对象：{c2}')

# <__main__.Car object at 0x12830a5d0> 汽车在跑...
c2.run()
print('-' * 34)

# 我是work函数，我的self值：<__main__.Car object at 0x12830a5d0>
# <__main__.Car object at 0x12830a5d0> 汽车在跑...
c2.work()
