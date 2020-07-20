import pygame.ftfont
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """显示的得分信息的类"""
    def __init__(self,ai,screen,stats):
        """初始化显示得分设计的属性"""
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.ai=ai
        self.stats=stats



        #显示得分信息时使用的字体设置
        self.text_color=(30,30,30)
        self.font=pygame.ftfont.SysFont(None,48)

        #准备初始得分的图形
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        #飞船图标
        self.prep_ships()
    def prep_ships(self):
        """显示还有多少飞船"""
        self.ships=Group()
        for ship_num in range(self.stats.ships_left):
            ship=Ship(self.ai,self.screen)
            ship.rect.x=10+ship_num*ship.rect.width
            ship.rect.y=10
            self.ships.add(ship)

    #绘制飞船等级水平
    def prep_level(self):
        #将等级转化为渲染的图像

        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai.bg_color)

        # 将得分放在屏幕右上角
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom+10
     #绘制当前分数
    def prep_score(self):
        """将得分转化为一副渲染的图像"""
        #分数数值取千分位，且取整
        rounded_score=int(round(self.stats.score,-1))
        score_str="{:,}".format(rounded_score)
        #score_str=str(self.stats.score)
        self.score_image=self.font.render(score_str,True,self.text_color,self.ai.bg_color)

        #将得分放在屏幕右上角
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20
    #绘制最高分数
    def prep_high_score(self):
        """将得分转化为一副渲染的图像"""
        # 分数数值取千分位，且取整
        rounded_score = int(round(self.stats.high_score, -1))
        score_str = "{:,}".format(rounded_score)
        # score_str=str(self.stats.score)
        self.high_score_image = self.font.render(score_str, True, self.text_color, self.ai.bg_color)

        # 将得分放在屏幕右上角
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    #将绘制的内容，显示到屏幕上
    def show_score(self):
        #在屏幕上显示最高得分与当前分数
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        #绘制飞船到屏幕
        self.ships.draw(self.screen)