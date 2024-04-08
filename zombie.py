import pygame.image

import image


class zombie(image.image):
    def __init__(self, pathmat, pathindex, pos, size, imagestute, pathindexcout=0):
        super().__init__(pathmat, pathindex, pos, size, imagestute, pathindexcout)
        # 碰撞体
        self.lasttime = 0
        self.collision = list()
        self.attackflag = 0
        self.collision.append((self.pos[0] + 80, self.pos[1] + 40))
        self.collision.append((self.pos[0] + 80, self.pos[1] + self.size[1]))

    def doleft(self):
        super().doleft()
        # 更新碰撞体
        self.collision[0] = (self.pos[0] + 80, self.pos[1] + 60)
        self.collision[1] = (self.pos[0] + 80, self.pos[1] + self.size[1])

    def updateindex(self, pathindex, nowtime):
        # 植物的动画帧数，我也不太懂，只能用时间差
       if self.attackflag == 1:
           if nowtime - self.lasttime >= 80:
               self.lasttime = nowtime
               super().updateindex(pathindex)
       else:
           self.lasttime = nowtime
           super().updateindex(pathindex)

    def attack(self, rect1):
        a1 = (rect1.pos[0] + rect1.size[0], rect1.pos[1])
        if self.collision[0][0] - 10 == a1[0] and self.attackflag == 0:
            self.pathmat = 'resourse/deadperson/normal/attack/ZombieAttack_'
            self.pathindex = 0
            self.pathindexcout = 20
            self.attackflag = 1
        elif self.attackflag == 0:
            self.pathmat = 'resourse/deadperson/normal/Zombie/Zombie_'
            self.attackflag = 0
            self.pathindexcout = 22

    def isCollision(self, rect1):
        if rect1.collision[1][0] >= self.collision[1][0] and self.collision[0][1] <= rect1.collision[1][1] <= \
                self.collision[1][1]:
            return True
        else:
            return False

    def active(self, screen,nowtime):
        if self.attackflag == 0:
            self.doleft();  # 碰撞检测
        self.draw(screen)
        self.updateindex(self.pathindex + 1,nowtime)
