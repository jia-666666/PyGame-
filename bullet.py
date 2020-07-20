import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类."""

    def __init__(self, ai, screen, ship):
        """在飞船所在位置创建一个子弹对象."""
        super().__init__()
        self.screen = screen

        # 在0.0坐标处创建一个表示子弹的矩形，在设置正确的位置
        self.rect = pygame.Rect(0, 0, ai.bullet_widths,ai.bullet_heights)

        #子弹的x坐标为飞船的x坐标，子弹的头为飞船的头，形象表示子弹从飞船发射
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)
        #子弹颜色与速度设置
        self.color = ai.bullet_color
        self.speed_factor = ai.bullet_speed

    def update(self):
        """向上移动子弹."""
        # 更新表示子弹位置的小数值.
        self.y -= self.speed_factor
        # 更新子弹的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """把子弹绘到屏幕上."""
        pygame.draw.rect(self.screen, self.color, self.rect)
