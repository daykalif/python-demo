import pygame

pygame.init()
screen = pygame.display.set_mode((320, 568))
bg = pygame.image.load("./img/background.png")
screen.blit(bg, (0, 0))
pygame.display.update()

while True:
    # 如果想要运行pygame，则需要将环境切换为/User/wangjiaping/minicidonda3/envs/snakes/bin/python3
    # mac,需要执行以下代码：循环事件 -- 兼容性问题 （windwos不需要循环事件，原因未知）
    for event in pygame.event.get():
        print(event.type, pygame.USEREVENT)
    pygame.display.update()
