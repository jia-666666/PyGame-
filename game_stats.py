class GameState():
    """跟踪游戏的统计信息"""
    def __init__(self,ai):
        """初始化统计信息"""
        self.ai=ai
        self.reset_stats()
        #游戏一开始是非活动状态
        self.game_active=False
        #游戏最高分
        self.high_score=0


    def reset_stats(self):
        """初始化游戏运行期间可能变化的统计信息"""
        self.ships_left=self.ai.ship_limit
        #分数统计
        self.score=0
        self.level=1