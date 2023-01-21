"""
导入模块：
在导入模块时，建议按照以下顺序导入
1.官方标准模块导入
2.第三方模块导入
3.应用程序模块导入
"""
import random
import pygame

"""
封装游戏中所有需要使用的精灵类
提供游戏的相关工具
"""

"""
pygame.sprite.Sprite -- 存储图像数据image和位置rect的对象
image：记录图像数据
rect：记录在屏幕上的位置
update（*args）：更新精灵位置
kill（）：从所有数组中删除

精灵：
    封装图像image、位置rect和速度speed
    提供update()方法，根据游戏需求，更新位置rect
"""

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 320, 568)
# 刷新的帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        # 如果子类的父类不是object，则需要主动调用父类的初始化方法
        super().__init__()

        # 定义对象属性
        self.image = pygame.image.load(image_name)  # 精灵图像，使用image_name加载
        # image的get_rect()方法，可以返回pygame.Rect(0,0,图像宽，图像高)的对象
        self.rect = self.image.get_rect()  # 精灵大小，默认使用图像大小
        self.speed = speed  # 精灵移动速度，默认为1

    def update(self):
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        # 1.调用父类方法实现精灵的创建（image/rect/speed）
        super().__init__("./img/background.png")
        # 2.判断是否是交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 1.调用父类的方法实现
        super().update()

        # 2.判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        # 1.调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("./img/smallplane.png")
        # 2.指定敌机的初始随机速度1-3
        self.speed = random.randint(1, 3)
        # 3.指定敌机的初始随机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 1.调用父类方法，保持垂直方向的飞行
        super().update()
        # 2.判断是否飞出屏幕，如果是，则需要从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            # print("飞出屏幕，需要从精灵组删除...")
            # kill方法可以将精灵从所有精灵组中移出，精灵就会被自动销毁
            self.kill()

    def __del__(self):
        # print("敌机挂了 %s" % self.rect)
        pass


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self, speedy=0):
        # 1.调用父类方法，设置image&speed
        super().__init__("./img/myplane.gif", 0)

        # 2.设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        self.speedy = speedy

        # 3.创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 英雄在水平和垂直方向移动
        self.rect.x += self.speed
        self.rect.y += self.speedy

        # 控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.bottom > SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom

    def fire(self):
        print("发射子弹...")

        for i in (0, 1, 2):
            # 1.创建子弹精灵
            bullet = Bullet()

            # 2.设置精灵的位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx

            # 3.将精灵添加到精灵组
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):
        # 调用父类方法，设置子弹图片，设置初始速度
        super().__init__("./img/bullet.png", -2)

    def update(self):
        # 调用父类方法，让子弹沿垂直方向飞行
        super().update()

        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹被销毁...")
        pass
