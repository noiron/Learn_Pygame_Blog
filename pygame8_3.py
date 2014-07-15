# -*- coding:utf8 -*-
 
# 本文件代码来自目光博客《用Python和Pygame写游戏-从入门到精通（8）》
# 产生动画和控制帧率
# http://eyehere.net/2011/python-pygame-novice-professional-8/

# 程序功能：在之前程序的基础上进行修改，使图片在碰到屏幕边缘后会反方向运动

# 需要注意的地方：tick()的用法

background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)

# Clock 对象
clock = pygame.time.Clock()

x, y = 100., 100.
# 速度（像素/秒）
speed_x, speed_y = 133., 170.

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, y))

    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0

    x += time_passed_seconds * speed_x
    y += time_passed_seconds * speed_y


    # 图片右侧到达边界，即反向运动
    if x > 640 - sprite.get_width():
        speed_x = - speed_x
        x = 640 - sprite.get_width()
    elif x < 0:
        speed_x = - speed_x
        x = 0.

    if y > 480 - sprite.get_height():
        speed_y = -speed_y
        y = 480 - sprite.get_height()
    elif y < 0:
        speed_y = -speed_y
        y = 0
        
    pygame.display.update()