"""
类是一个特殊的对象：
python中一切皆对象：
    class AAA:定义的类属于类对象
    obj1 = AAA() 属于实例对象

在程序运行时，类同样会被加载到内存
在python中，类是一个特殊的对象 -- 类对象
在程序运行时，类对象在内存中只有一份，使用一个类可以创建出很多个对象实例
除了封装实例的属性和方法外，类对象还可以拥有自己的属性和方法

1.类属性
2.类方法
通过 类名. 的方式可以访问类的属性 或者调用类的方法
"""


class Tool(object):
    # 使用赋值语句定义类属性，记录所有工具对象的数量
    # 类属性就是给类对象中定义的属性
    # 通常用来记录与这个类相关的特征
    # 类属性不会用于记录具体对象的特征
    count = 0

    def __init__(self, name):
        self.name = name

        # 让类属性的值+1
        Tool.count += 1


# 1.创建工具对象
tool1 = Tool("斧头")
# 2.输出工具对象总数
print(tool1.count)

tool2 = Tool("榔头")
print(tool2.count)

tool3 = Tool("水桶")
# 在python中属性的获取存在一个向上查找机制
print(Tool.count)  # 推荐使用这种：类名.类属性       ----> 类属性
print(tool3.count)  # 不推荐使用这种：对象.类属性

# 注意：如果要使用 对象.类属性 = 值 赋值语句，只会给对象添加一个属性，而不会影响到类属性的值
tool3.count = 99
print("工具对象总数：%d" % tool3.count)
print("===》 %d" % Tool.count)
