"""
静态方法：
在开发时，如果需要在类中封装一个方法，这个方法：
    既不需要 访问 实例属性 或者 实例方法
    也不需要 访问 类属性 或者 类方法
这个时候，可以把这个方法封装成一个静态方法

静态方法需要用修饰器@staticmethod来标识，告诉解释器这是一个静态方法
通过 类名. 调用 静态方法 -- 不需要创建对象
"""


class Dog(object):
    tone = 1

    @staticmethod
    def run():
        # 不访问实例属性/类属性
        print("小狗要跑...")

    def eat(self):
        print("小狗吃 %d 块骨头" % self.tone)

    def __init__(self, name):
        self.name = name


# 通过类名.调用静态方法 -- 不需要创建对象
Dog.run()
