import pygame.image


class image:
    def __init__(self, pathmat, pathindex, pos, size, imagestute, pathindexcout=0):
        self.pathmat = pathmat
        self.pathindex = pathindex
        self.pathindexcout = pathindexcout
        self.pos = list(pos)
        self.size = size
        # 用imagestate来描述当前图片的状态,就这样写把，这个地方是真不想动脑筋
        # 0 帧动画
        # 1 静态动画
        # 2 一张图片
        self.imagestute = imagestute
        if self.imagestute == 0:
            self.image = pygame.image.load(self.pathmat + str(pathindex) + ".png")
            self.image = pygame.transform.scale(self.image, self.size)
        elif self.imagestute == 1:
            self.image = pygame.image.load(self.pathmat)
            self.image = pygame.transform.scale(self.image, self.size)

    def updateimage(self):
        path = self.pathmat
        if self.pathindexcout != 0:
            path = self.pathmat + str(self.pathindex % self.pathindexcout) + '.png'
            print(path)
        self.image = pygame.image.load(path)
        if self.size:
            self.image = pygame.transform.scale(self.image, self.size)

    # 适应图片的大小
    def updatesize(self, size):
        self.size = size
        self.updateimage()

    # 更新图片的索引，帧动画
    def updateindex(self, pathindex):
        self.pathindex = pathindex
        self.updateimage()

    # 绘制
    def draw(self, ds):
        ds.blit(self.image, self.getrect())

    # 这段用来移动地图可以，也可以用来作用于人物的移动
    def doleft(self):
        self.pos[0] -= 1

    # 用来获得图片的坐标

    def getrect(self):
        rect = self.image.get_rect();
        rect.x, rect.y = self.pos
        return rect
