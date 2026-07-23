"""
多继承
"""


class Car:
    def __init__(self, brand, model, color, owner):
        print("Car的__init__方法")
        # 公有属性
        self.brand = brand  # 品牌
        self.model = model  # 型号
        self.color = color  # 颜色

        # 私有属性
        self.__owner = owner  # 拥有者

    def run(self):  # 行驶
        print(f'{self.brand} {self.model} 正在行驶...')


# 华为智驾
class HuaweiAiDriving:
    def __init__(self, version="V1.0"):
        self.version = version

    def run(self):
        print(f"使用华为AI智能辅助驾驶系统{self.version}正则驾驶...")


# 问界汽车
class WenJieCar(Car, HuaweiAiDriving):
    def __init__(self, brand, model, color, owner, version="V1.0"):
        Car.__init__(self, brand, model, color, owner)  # 等同于 super().__init__(brand, model, color, owner)
        HuaweiAiDriving.__init__(self, version)

    def run(self):
        Car.run(self)
        HuaweiAiDriving.run(self)


if __name__ == '__main__':
    car = WenJieCar("BMW", "X5", "红色", "张三")
    print(car)

    # MRO：方法解析顺序
    print(WenJieCar.__mro__)
    print(WenJieCar.mro())

    # 获取对象的属性字典
    print(car.__dict__)

    car.run()
