import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameState
from button import Button
#导入计分板
from scoreboard import Scoreboard


def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    #实例化settings对象
    ai=Settings()
    #创建游戏窗口大小
    screen=pygame.display.set_mode((ai.screen_width,ai.screen_height))
    #创建游戏标题
    pygame.display.set_caption("外星人大战")

    #创建按钮
    play_button=Button(ai,screen,"Play")

    bg_color=(230,230,230)
    #实例化飞船对象ship,传入屏幕实参
    ship=Ship(ai,screen)

    #创建一个用于存储游戏统计信息的实例，并创建计分板
    stats=GameState(ai)
    sb=Scoreboard(ai,screen,stats)

    #创造一个用于存储子弹和外星人的编组
    bullets=Group()
    aliens=Group()

    #创建外星人群
    gf.create_fleet(ai,screen,ship,aliens)

    #开始游戏的主循环
    while True:

        gf.check_events(ai, screen, stats, sb,play_button, ship, aliens, bullets)
        if stats.game_active:


            ship.update()
            gf.update_bullets(ai,screen,stats,sb,ship,aliens,bullets)

            gf.update_aliens(ai,stats,screen,sb,ship,aliens,bullets)

        gf.update_screen(ai,screen,stats,sb,ship,aliens,bullets,play_button)


if __name__ == '__main__':
    run_game()