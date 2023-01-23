import pygame
from plane_sprites import *

# 提示：python中并没有真正意义的常量，只是通过命名的约定
# --所有字母都是大写的就是常量，开发时不要轻易的修改


# 导入并初始化所有pygame模块，使用其他模块之前，必须先调用init方法
pygame.init()

# 编写游戏代码
print("游戏代码...")

"""
pygame专门提供了一个类，pygame.Rect用于描述矩形区域
pygame.Rect是一个比较特殊的类，内部只是特殊封装了一些数字计算
不执行pygame.init()方法同样能够直接使用
"""
hero_rect = pygame.Rect(100, 500, 120, 125)
print("英雄的原点 %d %d" % (hero_rect.x, hero_rect.y))
print("英雄的尺寸 %d %d" % (hero_rect.width, hero_rect.height))
print("%d %d" % hero_rect.size)  # size属性返回的是元祖属性，size的第一个值是矩形的宽度，size的第一个值是矩形的高度

"""
pygame专门提供了一个模块pygame.display用于创建，管理游戏窗口
参数：
    resolution指定屏幕的宽和高，默认创建的窗口大小和屏幕大小一致
    flags参数指定屏幕的附加选项，例如是否全屏等等，默认不需要传递
    depth参数表示颜色的位数，默认自动匹配

返回值：
    暂时可以理解为游戏的屏幕，游戏的元素都需要被绘制到游戏的屏幕上
注意：
    必须使用变量记录set_mode方法的返回结果！因为：后续所有的图像绘制都基于这个返回结果

pygame.display.set_mode(resolution=(0,0),flags=0,depth=0) -> Surface # 初始化游戏显示窗口
pygame.display.update()  # 刷新屏幕内容显示，稍后使用
"""
screen = pygame.display.set_mode((320, 568))

"""
图像文件初始是保存在磁盘上的，如果需要使用，第一步就需要被加载到内存
要在屏幕上看到某一个图像的内容，需要按照三个步骤：
1.使用pygame.image.load(file_path)加载图像的数据，
2.使用游戏屏幕对象，调用blit(图像,位置)方法将图像绘制到指定位置
3.调用pygame.display.update()方法更新整个屏幕的显示

提示：
    要想在屏幕上看到绘制的结果，就一定要调用pygame.display.update()方法
"""
# 绘制背景图像
# 1>加载图像数据
bg = pygame.image.load("./img/background.png")
# 2>blit(图像,位置) 绘制图像
screen.blit(bg, (0, 0))

# 绘制英雄的飞机
hero = pygame.image.load("./img/myplane.gif")
screen.blit(hero, (130, 400))

# 3>update更新屏幕显示,每秒调用60次动画效果，即可达到60帧，形成连贯的动画效果
pygame.display.update()

"""
游戏时钟：
pygame专门提供了一个类，pygame.time.Clock可以非常方便的设置屏幕绘制速度--刷新帧率
要使用时钟对象需要两步：
1).在游戏初始化创建一个时钟对象
2).在游戏循环中让时钟对象调用tick(帧率）方法
tick方法会根据上次被调用的时间，自动设置游戏循环中的延时
"""
# 创建时钟对象
clock = pygame.time.Clock()

# 1.定义rect记录飞机的初始位置
hero_rect = pygame.Rect(130, 400, 66, 80)

# 创建敌机的精灵
enemy = GameSprite("./img/smallplane.png", 2)
enemy1 = GameSprite("./img/midplane.png")

"""
pygame.sprite.Group
__init__(self,*精灵)
add(*sprites):向组中增加精灵
sprites():返回所有精灵列表
update(*args):让组中所有精灵调用update方法
draw(Surface):将组中所有的精灵的image，绘制到Surface的rect位置

精灵组：
    包含多个精灵对象
    update方法，让精灵组中的所有精灵调用update方法更新位置
    draw(screen)方法，在screen上绘制精灵组中的所有精灵
"""
# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)

"""
游戏循环：
为了做到游戏程序启动后，不会立即退出，通常会在游戏程序中增加一个游戏循环，
所谓游戏循环就是一个无限循环
在创建游戏窗口代码下方，增加一个无限循环

注意：游戏窗口不需要重复创建
"""
while True:
    # 可以指定循环体内部的代码执行的频率
    clock.tick(60)

    # 捕获事件
    # pygame中通过pygame.event.get()可以获得用户当前所做动作的事件列表
    # 用户可以同一时间做很多事情
    # 提示：这段代码非常的固定，几乎所有的pygame游戏都大同小异
    for event in pygame.event.get():
        # 判断用户是否点击了关闭按钮
        if event.type == pygame.QUIT:
            print("退出游戏..")
            # quit()卸载所有的模块
            pygame.quit()

            # 退出系统，直接终止当前正在执行的程序
            exit()

    # 2.修改飞机的位置
    hero_rect.y -= 1
    # 判断飞机的y值
    if hero_rect.y <= -80:
        hero_rect.y = 568

    # 3.调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 让精灵组调用两个方法
    # update - 让组中所有的精灵更新位置
    enemy_group.update()
    # draw - 在screen上绘制所有的精灵
    enemy_group.draw(screen)

    # 4.调用update方法更新显示
    pygame.display.update()

pygame.quit()  # 卸载所有pygame模块，在游戏结束之前调用！
