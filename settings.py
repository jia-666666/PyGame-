class Settings():
    """存储《外星人入侵》的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width=800
        self.screen_height=600
        self.bg_color=(230,230,230)

        #子弹设置
        self.bullet_speed=3
        self.bullet_widths=3
        self.bullet_heights=15
        self.bullet_color=60,60,60
        self.bullet_nums=300

        #外星人的设置
        self.alien_speed_factor=1
        self.fleet_drop_speed=5
        #ffleet_dirrection为1表示向右，-1xiangz向左
        self.fleet_direction=1
        #外星人点数提高速度
        self.score_scale=1.5

        #飞船设置
        self.ship_speed_factor=1.5
        self.ship_limit=3

        #以什么样的速度加快游戏节奏
        self.speedup_scale=1.1

        self.inits_reset_settings()

    #用于飞船碰撞死亡时，重置速度相关设置
    def inits_reset_settings(self):
        """初始化随游戏进行而变化的设置"""
        #初始化游戏的飞船子弹，外星人移动速度
        self.ship_speed_factor=1.5
        self.bullet_speed=30
        self.alien_speed_factor=1
        #外星人积分
        self.alien_points=50

        #fleet_directions左右方向标志
        self.fleet_direction=1
    #用于飞船射杀所有外星人后，游戏难度升级
    def increase_speed(self):
        """提高速度设置,增加游戏难度"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed_factor  *= self.speedup_scale

        self.alien_points=int(self.alien_points*self.score_scale)
