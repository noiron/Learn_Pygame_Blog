# -*- coding:utf8 -*-

  
# 本文件代码来自目光博客《用Python和Pygame写游戏-从入门到精通（1）》
# 理解游戏中的事件
# http://eyehere.net/2011/python-pygame-novice-professional-2/

background_image_filename = 'sushiplate.jpg'

import pygame
from pygame.locals  import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
background = pygame.image.load(background_image_filename).convert()

x, y = 0, 0
move_x, move_y = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        # 如果有键按下
        if event.type == KEYDOWN:
            # 按下的是左方向键的话，把x坐标减1
            if event.key == K_LEFT:
                move_x = -1
            elif event.key == K_RIGHT:
                move_x = 1
            # 上方向键，需要把y坐标减1，而不是加1
            elif event.key == K_UP:     
                move_y = -1
            elif event.key == K_DOWN:
                move_y = 1
        elif event.type == KEYUP:
            # 如果用户放开了键盘，图就不要动了
            move_x = 0
            move_y = 0

        # 计算出新的坐标
    x += move_x
    y += move_y

    screen.fill((23, 62, 125))      # 设置显示的背景色
    screen.blit(background, (x, y)) # 在新的位置上画图
    pygame.display.update()    # 显示图形必要的一部

