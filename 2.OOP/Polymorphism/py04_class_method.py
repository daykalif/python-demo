"""
类属性就是针对类对象定义的属性
    使用赋值语句在class关键字下方可以定义类属性
    类属性用于记录与这个类相关的特性
类方法就是针对类对象定义的方法
    在类方法内部可以直接访问类属性或者调用其他的类方法


类方法需要用修饰器 @classmethod 来标志，告诉解释器这是一个类方法
类方法的第一个参数应该是cls
    由哪一个类调用的方法，方法内的cls就是哪一个类的引用
    这个参数和实例方法的第一个参数是self类似
    提示使用其他名称也可以，不过习惯使用cls

通过 类名.调用类方法，调用方法时，不需要传递cls参数

在方法内部：
    可以通过cls.访问类的属性
    也可以通过cls.调用其他的类方法
"""


class Tool(object):
    count = 0

    @classmethod
    def show_tool_count(cls):
        print("工具对象总数：%d" % cls.count)

    def __init__(self, name):
        self.name = name
        Tool.count += 1


tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")

Tool.show_tool_count()
