import pygame
import sys

screen = pygame.display.set_mode((900, 600))
image = pygame.image.load('E:\外星人入侵\images\ship1.png')  # 加载图片并赋值给image
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((111, 111, 111))

    img_rect = image.get_rect()  # 获取图片的矩形区域
    screen_rect = screen.get_rect()  # 获取窗口的矩形区域
    img_rect.centerx = screen_rect.centerx  # 将窗口的矩形x坐标值赋值给图片的矩形x坐标值
    img_rect.bottom = screen_rect.bottom  # 如上
    screen.blit(image, img_rect)  # 在screen上绘制image图片，第二个参数为目标位置
    pygame.display.flip()
