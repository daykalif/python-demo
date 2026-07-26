"""
案例: 演示抽象类的用法.

抽象类解释:
    概述:
        在Python中, 抽象类 = 接口, 即: 有抽象方法的类就是 抽象类, 也叫 接口.
        抽象方法 = 没有方法体的方法, 即: 方法体是 pass 修饰的.
    作用/目的:
        抽象类一般充当父类, 用于指定行业规范, 准则, 具体地实现交由 子类 来完成.
"""


# 1. 定义抽象类，空调类，设定：空调的规则.
class AC:
    # 1.1 制冷
    def cool_wind(self):
        pass

    # 1.2 制热
    def hot_wind(self):
        pass

    # 1.3 左右摆风
    def swing_l_r(self):
        pass


# 2. 定义子类(小米空调)，实现父类(空调类)中的所有抽象方法.
class XiaoMi(AC):
    # 2.1 制冷
    def cool_wind(self):
        print('小米 核心 制冷技术!')

    # 2.2 制热
    def hot_wind(self):
        print('小米 核心 制热技术!')

    # # 2.3 左右摆风 （python中，抽象类可以不用强制重写；java中必须重写）
    # def swing_l_r(self):
    #     print('小米空调 静音左右摆风 技术!')


# 3. 定义子类(格力空调)，实现父类(空调类)中的所有抽象方法.
class Gree(AC):
    # 3.1 制冷
    def cool_wind(self):
        print('格力 核心 制冷技术!')

    # 3.2 制热
    def hot_wind(self):
        print('格力 核心 制热技术!')

    # 3.3 左右摆风
    def swing_l_r(self):
        print('格力空调 低频左右摆风 技术!')


# 4. 测试
if __name__ == '__main__':
    # 4.1 小米空调
    xm = XiaoMi()
    xm.cool_wind()
    xm.hot_wind()
    # xm.swing_l_r()
    print('-' * 23)

    # 4.2 格力空调
    gree = Gree()
    gree.cool_wind()
    gree.hot_wind()
    gree.swing_l_r()
