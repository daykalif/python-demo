# 子类继承自父类，可以直接享受父类中已经封装好的方法，不需要再次开发
# 子类中应该根据职责，封装子类特有的属性和方法

# 专业术语：
# Dog类是Animal类的子类，Animal类是Dog类的父类，Dog类从Animal类继承
# Dog类是Animal类的派生类，Animal类是Dog类的基类，Dog类从Animal类派生

# 继承的传递性：子类拥有父类以及父类的父类中封装的所有属性和方法


class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog(Animal):
    # 子类拥有父类的所有属性和方法
    def dark(self):
        print("汪汪叫")


class Cat(Animal):
    def catch(self):
        print("抓老鼠")


class XiaoTian(Dog):
    def fly(self):
        print("我会飞")


wangcai = XiaoTian()
wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.dark()
wangcai.fly()
# wangcai.catch()  wangcai这个对象并不能调用Cat类的方法
