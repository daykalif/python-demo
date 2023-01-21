class Dog:
    def dark(self):
        print("汪汪叫")

    def eat(self):
        print("吃")


class XiaoTian(Dog):
    def fly(self):
        print("我会飞")

    # 第一种：如果子类中，重写了父类的方法，在使用子类对象调用方法时，会调用子类中重写的方法
    def dark(self):
        print("啸天犬汪汪叫")

    def eat(self):
        # 1.针对子类特有的需求，编写代码
        print("啸天犬吃")

        # 2.第二种：使用super(),调用原来在父类中封装的方法
        super().eat()

        # 第三种：父类名.方法(self)
        Dog.eat(self)
        # 注意：如果使用子类调用方法，会出现递归调用-死循环！
        # XiaoTian.eat(self)

        # 3.增加其他子类的代码
        print("啸天犬别的方法")


wangcai = XiaoTian()
wangcai.dark()
wangcai.fly()
wangcai.eat()
