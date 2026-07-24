"""
案例：烤地瓜案例。

需求：
1. 定义地瓜类 → SweetPotato
2. 属性：被烤时间cook_time，烘焙状态 cook_state，调料 condiments
3. 行为：烘烤cook()，添加调料 add_condiment()
4. 魔法方法：init() → 初始化属性， str() → 打印地瓜信息。
5. 规则：
    烘烤时间        地瓜状态          包左不包右，前闭后开。
    [0, 3)         生的
    [3, 7)         半生不熟
    [7, 12)        熟了
    [12, ∞]        糊了
"""


# 1. 定义地瓜类 → SweetPotato
class SweetPotato:
    # 2. 在魔法方法__init__()中，初始化地瓜的属性.（有参，因为地瓜的初始状态是固定的）
    def __init__(self):
        self.cook_time = 0
        self.cook_state = '生的'
        self.condiments = []

    # 3.具体的烘烤动作.
    def cook(self, time):
        # 3.1 根据烘烤时间，修改地瓜的烘烤状态.
        if time <= 0:
            print('无效值！')
        else:
            # 3.2 修改地瓜的 烘烤时间.
            self.cook_time += time
            # 3.3 根据烘烤时间，修改地瓜的烘烤状态.
            if 0 <= self.cook_time < 3:
                self.cook_state = '生的'
            elif 3 <= self.cook_time < 7:
                self.cook_state = '半生不熟'
            elif 7 <= self.cook_time < 12:
                self.cook_state = '熟了'
            else:
                self.cook_state = '糊了'

    # 4. 添加调料 add_condiment()
    def add_condiment(self, condiment):
        self.condiments.append(condiment)

    # 5. 重写str()方法，打印地瓜信息.
    def __str__(self):
        return f'烘烤时间: {self.cook_time}, 地瓜状态: {self.cook_state}, 调料: {self.condiments}'


# 6.测试.
if __name__ == '__main__':
    # 7. 创建地瓜对象
    dg = SweetPotato()

    # 8. 具体的烘烤动作.
    # dg.cook(-3)
    dg.cook(3)
    dg.cook(5)
    dg.cook(7)

    # 9. 添加调料
    dg.add_condiment('芥末/辣根')
    dg.add_condiment('折耳根')
    dg.add_condiment('豆汁')
    dg.add_condiment('鲱鱼罐头')

    # 10. 打印地瓜状态.
    print(dg)
