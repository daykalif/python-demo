"""
继承：描述的是两个类之间的关系，子类继承父类，就可以获取到父类中非私有的属性和方法
"""


class Car:
    # 这个不是私有方法
    def __init__(self, brand, model, color, owner):
        # 公有属性
        self.brand = brand  # 品牌
        self.model = model  # 型号
        self.color = color  # 颜色

        # 私有属性
        self.__owner = owner  # 拥有者

    def start(self):  # 启动
        print(f'{self.brand} {self.model} 正在启动...')

    def run(self):  # 行驶
        print(f'{self.brand} {self.model} 正在行驶...')

    def stop(self):  # 停止
        print(f'{self.brand} {self.model} 停止行驶...')

    def charge(self):
        print(f'{self.brand} {self.model} 正在补充燃料...')

    # 公有方法中加工返回私有属性
    def get_owner(self):
        return self.__owner[0:1] + '**'  # 返回所有者姓名的首字母加**

    # 私有方法
    def __control_fuel(self):
        print(f'{self.brand} {self.model} 正在控制燃油...')


# 燃油车
class FuelCar(Car):
    # 重写父类的charge方法
    def charge(self):
        print(f'{self.brand} {self.model} 正在补充燃油...')


# 电车
class ElectricCar(Car):
    # 重写父类的charge方法
    def charge(self):
        # 调用父类的charge方法

        # 方式一：super().方法名()
        # super().charge()

        # 方式二：父类名.方法(self)
        Car.charge(self)

        # 重写自己的charge方法
        print(f'{self.brand} {self.model} 正在补充电能...')


if __name__ == '__main__':
    c1 = FuelCar('BMW', 'X5', '红色', '张三')

    print(c1.brand)
    print(c1.color)

    c1.start()
    c1.run()
    c1.stop()

    c1.charge()

    # 可获取
    print(c1.get_owner())
    print(c1._Car__owner)

    # 不可获取
    # print(c1.__owner)

    c2 = ElectricCar('Tesla', 'Model S', '白色', '李四')
    c2.charge()
