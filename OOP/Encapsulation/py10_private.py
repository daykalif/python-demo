# 添加私有属性或私有方法，只需在属性名或方法名前添加两个下划线
class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        # 在对象的方法内部，是可以访问对象的私有属性的
        print("%s 年龄是 %d" % (self.name, self.__age))


xiaofang = Women("小芳")

# 私有属性，在外界不能被直接访问
# print(xiaofang.__page)

# 私有方法，同样不允许在外界被访问
# xiaofang.__secret()


"""
伪私有属性和私有方法(科普)
提示：在日常开发中，不要使用这种方式，访问对象的私有属性或私有方法
python中，并没有真正意义的私有

在给属性，方法命名时，实际是对名称做了一些特殊处理，使得外界无法访问到
处理方式：在名称前面加上 _类名 => _类名__名称
"""

print(xiaofang._Women__age)
xiaofang._Women__secret()
