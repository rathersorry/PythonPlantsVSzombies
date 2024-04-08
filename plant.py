import image
import bullet


class plant(image.image):

    def __init__(self, pathmat, pathindex, pos, size, imagestute, pathindexcout=0):
        super().__init__(pathmat, pathindex, pos, size, imagestute, pathindexcout)
        self.bullets = list()
        self.lasttime = 0
        self.lastAttacktime = 0

    # 发射豌豆
    def attack(self, nowtime):
        if self.lastAttacktime == 0:
            self.lastAttacktime = nowtime
        elif nowtime - self.lastAttacktime >= 3000:
            self.bullets.append(bullet.bullet('resourse/plant/wandousheshou/attack/PeaNormal_0.png',
                                              self.pathindex
                                              , self.pos, (56, 34), 1))
            self.lastAttacktime = nowtime

    def updateindex(self, pathindex, nowtime):
        # 植物的动画帧数，我也不太懂，只能用时间差
        if nowtime - self.lasttime >= 70:
            self.lasttime = nowtime
            super().updateindex(pathindex)

    def checkbullets(self, screen, zombie, nowtime, texiao_1):
        for i in self.bullets:
            if not i.isdel:
                i.draw(screen)
                i.doleft()
            if zombie.isCollision(i) and not i.isdelte:
                i.ensureDel(nowtime)
                texiao_1.pos = ((zombie.collision[0][0] + zombie.collision[1][0]) / 2 - 20,
                                (zombie.collision[0][1] + zombie.collision[1][1]) / 2 - 45)
                texiao_1.draw(screen)

        # 如果检查到碰撞，就删除子弹,如果你把它写上面这段，子弹会闪烁，我没想出来为什么，
        for i in self.bullets:
            if i.isdel:
                self.bullets.remove(i)

    def delbullet(self, element):
        self.bullets.remove(element);
    def active(self, screen, nowtime, zombie_1, texiao):
        self.attack(nowtime)
        self.updateindex(self.pathindex + 1, nowtime)
        self.checkbullets(screen, zombie_1, nowtime, texiao)
        self.draw(screen)
