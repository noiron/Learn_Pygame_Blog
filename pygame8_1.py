# -*- coding:utf8 -*-
 
# 本文件代码来自目光博客《用Python和Pygame写游戏-从入门到精通（8）》
# 产生动画和控制帧率
# http://eyehere.net/2011/python-pygame-novice-professional-8/

# 程序功能：在显示窗口中，一张图片从左至右不停运动

background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)

# sprite 的起始坐标
x = 0.

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, 100))
    x += 0.1

    if x > 640.:
        x = 0.

    pygame.display.update()