"""
多态：
- 多态是指同一个方法，具有不同的表现形态
- 如：定义函数时，参数类型指定为父类类型，在执行的时候传入不同的子类对象，就具有不同的形态
"""


class Car:
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

    def get_owner(self):
        return self.__owner[0:1] + '**'


# 燃油车
class FuelCar(Car):
    def charge(self):
        print(f'{self.brand} {self.model} 正在补充燃油...')


# 电车
class ElectricCar(Car):
    def charge(self):
        print(f'{self.brand} {self.model} 正在补充电能...')


# 补充燃料函数
def handle_charge(car: Car):  # 函数参数类型声明 --- 指定的是父类型
    car.charge()


if __name__ == '__main__':
    handle_charge(FuelCar('BMW', 'X5', '红色', '张三'))  # 燃油车补充燃料
    handle_charge(ElectricCar('Tesla', 'Model S', '白色', '李四'))  # 电车补充燃料
