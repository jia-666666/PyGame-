import pygame,time
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai,screen):
        """初始化飞船并设置其初始位置"""
        super().__init__()
        self.screen=screen
        self.ai=ai

        #加载飞船图像
        self.image=pygame.image.load('images\ship.bmp')
        #获取飞船图像的长宽尺寸
        self.rect=self.image.get_rect()
        #获取游戏屏幕的尺寸
        self.screen_rect=screen.get_rect()


        #将每艘新飞船放在屏幕底部的中央

        #飞船的x坐标=屏幕的x中间位置坐标
        self.rect.centerx=self.screen_rect.centerx
        #飞船的y坐标=屏幕的底部Y值
        self.rect.bottom=self.screen_rect.bottom



        #飞船移动标志
        self.moving_right=False
        self.moving_left =False
        self.moving_down = False
        self.moving_up = False

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.y=self.screen_rect.bottom-50

    def update(self):

        """根据移动标志调整飞船的位置"""
        #更新飞船的center值而不是rect
        #
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.centery -= 1

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1


        self.rect.centerx = self.rect.centerx
        self.rect.centery = self.rect.centery


    def blitme(self):
        """指定位置绘制飞船"""

        #blit(图像，图像绘制的位置坐标)
        self.screen.blit(self.image,self.rect)

