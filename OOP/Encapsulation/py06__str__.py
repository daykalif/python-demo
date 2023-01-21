# __str__
# 在python中，使用print输出 对象变量 ，默认情况下，会输出这个变量引用当对象是由哪一个类创建的对象，以及在内存中的地址(十六进制表示)
# 如果在开发中，希望使用print输出对象变量时，能够打印自定义的内容，就可以利用__str__这个内置方法了
# 注意：__str__ 方法必须返回一个字符串


class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s来了" % self.name)

    def __del__(self):
        print("%s走了" % self.name)

    # 注意：__str__ 方法必须返回一个字符串
    def __str__(self):
        return "我是小猫：[%s]" % self.name


# tom 是一个全局变量
tom = Cat("tom")
print(tom)
