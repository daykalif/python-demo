"""
案例: 演示Python的多态案例之 战斗平台.

需求:
    1. 构建对战平台(公共的函数) object_play(), 接收: 英雄机 和 敌机.
    2. 在不修改对战平台代码的情况下, 完成多次战斗.
    3. 规则:
        英雄机, 1代战斗力60, 2代战斗力80
        敌机, 1代战斗力70

代码提示:
    英雄机1代 HeroFighter
    英雄机2代 AdvHeroFighter
    敌机      EnemyFighter
"""


# 1. 定义英雄机1代，战斗力 60
class HeroFighter:
    def power(self):
        return 60


# 2. 定义英雄机2代，战斗力 80
class AdvHeroFighter(HeroFighter):
    def power(self):
        return 80


# 3. 敌机1代
class EnemyFighter:
    def power(self):
        return 70


# 4. 构建对战平台，公共的函数，接收不同的参数，有不同的效果 → 多态.
def object_play(hero: HeroFighter, enemy: EnemyFighter):  # def object_play(hero, enemy):
    # 参1：英雄机，参2：敌机
    if hero.power() >= enemy.power():
        print('英雄机 战胜 敌机！')
    else:
        print('英雄机 惜败 敌机！')


# 5. 测试.
if __name__ == '__main__':
    # 思路1: 不使用多态，完成对战.
    # 场景1: 英雄机1代 vs 敌机1代
    h1 = HeroFighter()
    e1 = EnemyFighter()
    if h1.power() >= e1.power():
        print('英雄机1代 战胜 敌机1代')
    else:
        print('英雄机1代 惜败 敌机1代')
    print('-' * 34)

    # 场景2: 英雄机2代 vs 敌机1代
    h2 = AdvHeroFighter()
    e1 = EnemyFighter()
    if h2.power() >= e1.power():
        print('英雄机2代 战胜 敌机1代')
    else:
        print('英雄机2代 惜败 敌机1代')
    print('*' * 34)

    # 思路2：使用多态，完成对战.
    h1 = HeroFighter()
    h2 = AdvHeroFighter()
    e1 = EnemyFighter()
    # 场景1：英雄机1代 vs 敌机1代
    object_play(h1, e1)
    print('-' * 34)
    # 场景2：英雄机2代 vs 敌机1代
    object_play(h2, e1)

    # 多态添加类型后会警告，但python不会报错
    object_play(h2, h1)
