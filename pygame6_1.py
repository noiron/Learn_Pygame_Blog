# -*- coding:utf8 -*-
 
# 本文件代码来自目光博客《用Python和Pygame写游戏-从入门到精通（6）》
# 使用图像，理解Surface
# http://eyehere.net/2011/python-pygame-novice-professional-6/

# 程序功能：在屏幕上随机画点

import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    # 随机设置需要显示的颜色
    rand_col = (randint(0, 255), randint(0, 255), randint(0, 255))
    
    screen.lock()
    for _ in xrange(10):
        rand_pos = (randint(0, 639), randint(0, 479))   # 随机设置画点的位置
        screen.set_at(rand_pos, rand_col)   
    screen.unlock()
    pygame.display.update()
