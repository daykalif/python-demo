"""
封装：将数据(属性)和操作数据的方法绑定在一起，形成一个独立的单元(类)，保护数据不被外部访问，通过访问修饰符实现封装。
1. 私有属性：在属性名前加双下划线__
2. 私有方法：在方法名前加双下划线__
"""

"""
Python 没有语法级别的真正私有（不像 Java、C++），但__xxx双下划线会触发 名称改写（Name Mangling），直接访问对象.__属性名会找不到，因此报错。

1. 详细原理
当你写：
self.__owner = owner

Python 底层会自动把名字改写为：
_Car__owner，也就是：类名_原属性名

所以：
car.__owner → 代码寻找名字叫 __owner 的属性，不存在 → AttributeError 报错
car._Car__owner → 访问改写后的真实名字，可以拿到数据
这只是改名伪装，不是彻底封锁，所以业内说：Python 没有真正私有。
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

    # 公有方法中加工返回私有属性
    def get_owner(self):
        return self.__owner[0:1] + '**'  # 返回所有者姓名的首字母加**

    # 私有方法
    def __control_fuel(self):
        print(f'{self.brand} {self.model} 正在控制燃油...')


if __name__ == '__main__':
    car = Car(brand='Audi', model='A6', color='黑色', owner='张三')
    print(car.brand)
    print(car.model)
    print(car.color)

    # 调用车辆动作方法
    car.start()
    car.run()
    car.stop()

    # 调用公有方法获取私有属性
    owner = car.get_owner()
    print(owner)

    # 访问私有的属性值（使用加工后的名称）
    print(car._Car__owner)

    # 访问私有的属性值/方法（报错）
    print(car.__owner)
    print(car.__control_fuel)
