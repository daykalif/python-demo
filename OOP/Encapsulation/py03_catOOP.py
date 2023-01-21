class Cat:
    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print(" %s 爱吃鱼" % self.name)

    def drink(self):
        print("小猫要喝水")


# 创建一个猫对象
tom = Cat()

# 在python中，要给对象设置属性，非常的容易，但是不推荐使用，
#   因为：对象属性的封装应该封装在类的内部
# 只需要在类的外部的代码中直接通过 . 设置一个属性即可
# 注意：这种方式虽然简单，但是不推荐使用！
tom.name = "TOM"  # 可以使用 .属性名 利用赋值语句就可以了

tom.eat()
tom.drink()
print(tom)

# 再创建一个猫对象
lazy_cat = Cat()
lazy_cat.name = "大懒猫"
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)

# 下面这两只猫是同一只猫
lazy_cat2 = lazy_cat
print(lazy_cat2)
