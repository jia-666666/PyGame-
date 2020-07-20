import sys
from time import sleep

import pygame

from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai, screen, ship, bullets):

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai, screen, stats,sb, play_button, ship, aliens, bullets):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(ai, screen, stats,sb,play_button, ship, aliens, bullets, mouse_x, mouse_y)
def check_play_button(ai,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    """在玩家单击play按钮是开始游戏"""
    if not stats.game_active and play_button.rect.collidepoint(mouse_x,mouse_y):
        #隐藏光标
        pygame.mouse.set_visible(False)

        #重置游戏统计信息
        stats.reset_stats()

        #重置游戏设置
        ai.inits_reset_settings()
        stats.game_active=True

        #重置记分牌图像
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_score()
        sb.prep_ships()

        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        #创建一群新的外星人，并让飞船居中
        create_fleet(ai,screen,ship,aliens)
        ship.center_ship()


def fire_bullet(ai, screen, ship, bullets):

    if len(bullets) < ai.bullet_nums:
        new_bullet = Bullet(ai, screen, ship)
        bullets.add(new_bullet)

def update_screen(ai_settings, screen,stats,sb, ship, aliens, bullets,play_button):

    screen.fill(ai_settings.bg_color)


    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    #显示得分
    sb.show_score()
    #如果游戏处于非活动状态，就绘制按钮play
    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()

def update_bullets(ai, screen, stats,sb,ship, aliens, bullets):

    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai, screen, stats,sb,ship, aliens, bullets)

def check_bullet_alien_collisions(ai, screen, stats,sb,ship, aliens, bullets):
    #删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score+=ai.alien_points*len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)

    if len(aliens) == 0:
        bullets.empty()
        #游戏难度升级
        ai.increase_speed()
        #提高等级
        stats.level+=1
        sb.prep_level()


        create_fleet(ai, screen, ship, aliens)

def check_fleet_edges(ai, aliens):

    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai, aliens)
            break

def change_fleet_direction(ai, aliens):

    for alien in aliens.sprites():
        alien.rect.y += ai.fleet_drop_speed
    ai.fleet_direction *= -1

def ship_hit(ai, stats, screen, sb,ship, aliens, bullets):

    if stats.ships_left > 0:
        # Decrement ships_left.
        stats.ships_left -= 1
        sb.prep_ships()
    else:
        stats.game_active = False
        #光标显示
        pygame.mouse.set_visible(True)


    aliens.empty()
    bullets.empty()


    create_fleet(ai, screen, ship, aliens)
    ship.center_ship()

    # Pause.
    sleep(0.5)

def check_aliens_bottom(ai, stats, screen, ship, aliens, bullets):

    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:

            ship_hit(ai, stats, screen, ship, aliens, bullets)
            break

def update_aliens(ai, stats, screen, sb,ship, aliens, bullets):

    check_fleet_edges(ai, aliens)
    aliens.update()


    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai, stats, screen, sb,ship, aliens, bullets)


    check_aliens_bottom(ai, stats, screen, ship, aliens, bullets)

def get_number_aliens_x(ai, alien_width):

    available_space_x = ai.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai, ship_height, alien_height):

    available_space_y = (ai.screen_height -
                            (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai, screen, aliens, alien_number, row_number):

    alien = Alien(ai, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai, screen, ship, aliens):

    alien = Alien(ai, screen)
    number_aliens_x = get_number_aliens_x(ai, alien.rect.width)
    number_rows = get_number_rows(ai, ship.rect.height,
                                  alien.rect.height)


    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x+1):
            create_alien(ai, screen, aliens, alien_number,
                         row_number)
#判断是否生成最高分
def check_high_score(stats,sb):
    if stats.score>stats.high_score:
        stats.high_score=stats.score
        sb.prep_high_score()
