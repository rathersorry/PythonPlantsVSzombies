import image


class bullet(image.image):

    def __init__(self, pathmat, pathindex, pos, size, imagestute, pathindexcout=0):
        super().__init__(pathmat, pathindex, (pos[0] + size[0], pos[1]), size, imagestute, pathindexcout)
        # 碰撞体
        self.isdel = False
        self.lasttime = 0
        self.isdelte=False
        self.x = self.pos[0] + self.size[0] / 2
        self.y = self.pos[1] + self.size[1] / 2
        self.collision = list();
        self.collision.append((self.x, self.y))
        self.collision.append((self.x + 15, self.y))

    def getcollision(self):
        return self.collision

    def doleft(self):
        self.pos[0] += 5
        self.x = self.pos[0] + self.size[0] / 2
        self.y = self.pos[1] + self.size[1] / 2
        self.collision[0] = (self.x, self.y)
        self.collision[1] = (self.x + 15, self.y)

    def ensureDel(self, nowtime):
        self.isdel=True
        if self.lasttime == 0:
            self.lasttime = nowtime
        else:
            if nowtime - self.lasttime >= 65:
               self.isdelte=True
