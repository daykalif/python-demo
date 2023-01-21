# __del__ 方法：
# 在python中，当使用 类名() 创建对象时，为对象分配完空间后，自动调用 __init__ 方法
# 当一个对象被从内存中销毁前，会自动调用 __del__方法

# 应用场景：
# __init__ 改造初始化方法，可以让创建对象更加灵活
# __del__ 如果希望在对象被销毁前，再做一些事情，可以考虑一下 __del__ 方法


class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s来了" % self.name)

    def __del__(self):
        print("%s走了" % self.name)


# tom 是一个全局变量
tom = Cat("tom")
print(tom.name)

# del 关键字可以删除一个对象
del tom

print("-" * 50)
