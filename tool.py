import pygame
import main
import plant
import sumflower
import chomper


# 鼠标类，点击或者选择植物的逻辑
class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        self.hasPlant = 0
        self.image = pygame.Surface((2, 2))
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.rect.center = pygame.mouse.get_pos()  # 初始位置到鼠标指针
        self.click = False

    def getrect(self):
        rect = self.image.get_rect();
        rect.x, rect.y = (self.rect.center[0] - 25, self.rect.center[1] - 20)
        return rect

    def update(self, sf):
        self.rect.center = pygame.mouse.get_pos()  # 移到鼠标指针位置，有延迟，尽量用原生的getpos
        sf.blit(self.image, self.getrect())

    def check_plant(self, ds, list1, list2, plant_list):
        x = self.rect.center[0]
        y = self.rect.center[1]
        self.click = pygame.mouse.get_pressed()[0]
        if self.click:
            if 86 <= x <= 86 + 52 and 6 <= y <= 76:
                self.image = pygame.image.load('resourse/plant/wandousheshou/step/Peashooter_0.png')
                self.hasPlant = 1
            elif 141 <= x <= 141 + 52 and 6 <= y <= 76:
                self.image = pygame.image.load('resourse/plant/sunflower/SunFlower_0.png')
                self.hasPlant = 2
            elif 196 <= x <= 196 + 52 and 6 <= y <= 76:
                self.image = pygame.image.load('resourse/plant/photoMine/step/PotatoMine_s.png')
                self.hasPlant = 3
            elif 251 <= x <= 251 + 52 and 6 <= y <= 76:
                self.image = pygame.image.load('resourse/plant/wallnut/step/WallNut_0.png')
                self.hasPlant = 4
            elif 306 <= x <= 306 + 52 and 6 <= y <= 76:
                print("5")
            elif 361 <= x <= 361 + 52 and 6 <= y <= 76:
                print("6")
            elif pygame.mouse.get_pressed()[0]:
                self.image = pygame.Surface((1, 1))
                self.image.fill('red')
                self.plants(list1, list2, plant_list, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    def plants(self, list1, list2, plant_list, x, y):
        if self.hasPlant != 0 and self.click:
            print("ssssssss")
            z = 0
            t = 0
            # list1 是纵坐标，list2是横坐标，其实还可以用二分优化，我不想
            for i in list1:
                if i[0] <= y <= i[1]:
                    print([i[0], x, i[1]])
                    z = i[0]
                    break
            for i in list2:
                if i[0] <= x <= i[1]:
                    t = i[0]
                    break
            if z != 0 and t != 0:
                print([z, t])
                if self.hasPlant == 1:
                    plant_list.append(
                        plant.plant('resourse/plant/wandousheshou/step/Peashooter_', 0, (t, z), (80, 70), 0, 13))
                elif self.hasPlant == 2:
                    plant_list.append(
                        sumflower.sumflower('resourse/plant/sunflower/SunFlower_', 0, (t, z), (80, 70), 0, 18))
                elif self.hasPlant == 3:
                    plant_list.append(
                        sumflower.sumflower('resourse/plant/photoMine/step/PotatoMineInit_0(已去底).png', 0, (t, z), (75, 60), 1))
                elif self.hasPlant == 4:
                    plant_list.append(
                        sumflower.sumflower('resourse/plant/wallnut/step/WallNut_', 0, (t, z), (65, 73), 0, 16))
        self.hasPlant = 0

    def active(self, ds, plant_list, list1, list2):
        self.update(ds)
        self.check_plant(ds, list1, list2, plant_list)
