# 当使用 类名()创建对象时，会自动执行以下操作：
# 1.为对象在内存中 分配空间 -- 创建对象
# 2.为对象的属性设置 初始值 -- 初始化方法(init)
# 这个初始化方法就是 __init__ 方法，__init__ 是对象的内置方法
# __init__ 方法是专门用来定义一个类具有哪些属性的方法！


class Cat:
    def eat(self):
        print(" %s 爱吃鱼，今年 %s" % (self.name, self.age))

    def __init__(self, new_age):
        print("这是一个初始化方法")
        self.name = "汤姆"
        self.age = new_age


# 使用类名()创建对象的时候，会自动调用初始化方法__init__
tom = Cat("2岁")
print(tom.name)
tom.eat()

lazy_cat = Cat("3岁")
lazy_cat.eat()
