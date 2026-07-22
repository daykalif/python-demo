# 子类可以拥有多个父类，并且拥有所有父类的属性和方法
# 注意：开发时，应该尽量避免这种容易产生混淆的情况！-- 如果 父类之间存在同名的属性或者方法，应该尽量避免使用多继承


class A:
    def test(self):
        print("A---test 方法")


class B:
    def test(self):
        print("B---test 方法")

    def demo(self):
        print("B---demo 方法")


class C(A, B):
    """多继承可以让子类对象，同时具有多个父类的属性和方法"""

    pass


c = C()
c.test()
c.demo()

# Python中的MRO -- 方法搜索顺序
# python中针对类提供了一个内置属性 __mro__ 可以查看方法搜索顺序
# MRO是method resolution order，主要用于在多继承时判断方法、属性的调用路径
# 确定C类对象调用方法的顺序
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

"""
    新式类 与 旧式(经典)类
    object是python作为所有对象提供的基类，提供有一些内置的属性和方法，可以使用dir函数查看
    新式类：以object为基类的类，推荐使用
    经典类：不以object为基类的类，不推荐使用
    
    在python3.x中定义类时，如果没有指定父类，会默认使用object作为该类的基类 -- python3.x中定义的类都是新式类
    在python2.x中定义类时，如果没有指定父类，则不会以object作为基类
    class A(object):
        pass
    
    class B:
        pass
    
    新式类和经典类在多继承时 -- 会影响到方法的搜索顺序
    
    为了保证编写的代码能够同时在python2.x和python3.x运行！
    今后在定义类时，如果没有父类，建议统一继承自object
"""
