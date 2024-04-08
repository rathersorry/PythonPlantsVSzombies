import random
import sys
import pygame
import tool
import pygame.locals
import pygame
import image
import plant
import zombie
import bullet


def drawrect(screen, color, up_left, up_right, down_right=(0, 0), down_left=(0, 0)):
    pygame.draw.line(screen, color, up_left, up_right)
    pygame.draw.line(screen, color, up_left, down_left)
    pygame.draw.line(screen, color, down_left, down_right)
    pygame.draw.line(screen, color, up_right, down_right)


def maingame():
    pygame.init()
    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("motherfucker")
    mouse = tool.Mouse()
    # 植物选择框
    Plantbar = image.image('resourse/screnn/ChooserBackground.png', 0, (10, 0), (522, 87), 1)
    # 卡片加载
    card_1 = image.image('resourse/screnn/CARD/card_peashooter.png', 0, (86, 6), (52, 70), 1)
    card_2 = image.image('resourse/screnn/CARD/card_sunflower.png', 0, (141, 6), (52, 70), 1)
    card_3 = image.image('resourse/screnn/CARD/card_potatomine.png', 0, (196, 6), (52, 70), 1)
    card_4 = image.image('resourse/screnn/CARD/card_wallnut.png', 0, (251, 6), (52, 70), 1)
    card_5 = image.image('resourse/screnn/CARD/card_cherrybomb.png', 0, (306, 6), (52, 70), 1)
    # 小车
    # car=image.image('resourse/plant/screnn/car.png',0,(218,))
    # 背景
    img = image.image("resourse/background/Background_0.jpg", 0, (0, 0), (1200, 600), 1)
    # 僵尸加载大小
    zombie_1 = zombie.zombie('resourse/deadperson/normal/Zombie/Zombie_', 0, (800, 220), (140, 130), 0, 22)
    # 攻击特效
    texiao_1 = image.image('resourse/plant/wandousheshou/texiao/PeaNormalExplode_0.png', 0, (700, 220), (52, 46), 1)
    # 植物加载大小
    plant_1 = plant.plant('resourse/plant/wandousheshou/step/Peashooter_', 0, (210, 270), (80, 70), 0, 13)
    sunflower = plant.plant('resourse/plant/sunflower/SunFlower_', 0, (210, 370), (80, 70), 0, 18)
    # 上一次的时间
    plant_list = list()
    color = 255, 0, 0
    x = 77
    l_x = 1
    check_list_1 = list()

    # 初始化一下格子
    while x <= 570:
        l_x = x
        x += 99
        check_list_1.append([l_x, x])
    x = 215
    l_x = 215
    check_list_2 = list()
    while x <= 835:
        l_x = x
        x += 69
        check_list_2.append([l_x, x])
    for i in check_list_1:
        print(i)


    x=1
    lasttime=pygame.time.get_ticks()
    Clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        Clock.tick(13)
        # 地图，所有draw都要在这个下面
        img.draw(screen)
        card_1.draw(screen)
        Plantbar.draw(screen)
        # 卡片加载，避免被plantbar覆盖
        card_1.draw(screen)
        card_2.draw(screen)
        card_3.draw(screen)
        card_4.draw(screen)
        card_5.draw(screen)
        # 别管，我就喜欢这样写
        # for i in check_list_1:
        #     for j in check_list_2:
        #         drawrect(screen,color,(j[0], i[0]), (j[1], i[0]), (j[1], i[1]), (j[0], i[1]))

        zombie_1.active(screen,pygame.time.get_ticks())
        # pygame.draw.line(screen,color,zombie_1.collision[0],zombie_1.collision[1])
        mouse.active(screen, plant_list, check_list_1, check_list_2)

        for i in plant_list:
            i.active(screen, pygame.time.get_ticks(), zombie_1, texiao_1)
            zombie_1.attack(i)

        # 植物种植的判定范围
        # pygame.draw.line(screen, color, (215, 77), (835, 77))
        # pygame.draw.line(screen, color, (215, 77), (215, 570))
        # pygame.draw.line(screen, color, (215, 570), (835, 570))
        # pygame.draw.line(screen, color, (835, 77), (835, 570))
        # 在这儿更新植物动画\
        pygame.display.flip()


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    maingame()
