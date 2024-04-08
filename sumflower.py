import plant


class sumflower(plant.plant):
    def __init__(self, pathmat, pathindex, pos, size, imagestute, pathindexcout=0):
        super().__init__(pathmat, pathindex, pos, size, imagestute, pathindexcout)
        self.lasttime = 0
        self.lastAttacktime = 0

    def active(self, screen, nowtime, zombie_1, texiao):
        self.updateindex(self.pathindex + 1, nowtime)
        self.draw(screen)
