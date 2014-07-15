# -*- coding:utf8 -*-
 
# 本文件代码来自目光博客《用Python和Pygame写游戏-从入门到精通（8）》
# 产生动画和控制帧率
# http://eyehere.net/2011/python-pygame-novice-professional-8/

# 程序功能：通过设定统一的移动速率，保证图片在不同机器上移动得一样快

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

x = 0.
# 速度（像素/秒）
speed = 250.

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, 100))

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    distance_moved = time_passed_seconds * speed
    x += distance_moved

    if x > 640:
        x -= 640.

    pygame.display.update()