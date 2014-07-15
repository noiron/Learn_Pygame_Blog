# -*- coding:utf8 -*-
 
# 本文件代码来自目光博客《用Python和Pygame写游戏-从入门到精通（4）》
# 使用字体模块，Pygame 的错误处理
# http://eyehere.net/2011/python-pygame-novice-professional-4/

# 程序功能：在背景图片上，“你好”从屏幕右方向左移动

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

# 这里选择微软雅黑字体，选择英文字体时，可能会出现无法显示汉字的情况
# 如果找不到选择的字体，显示的将是两个方块
font = pygame.font.SysFont("microsoftyahei", 40)
text_surface = font.render(u"你好", True, (0, 0, 255))

x = 0
y = (480 - text_surface.get_height())/2

background = pygame.image.load("sushiplate.jpg").convert()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))

    # 改变x坐标，文字向左移动
    x -= 0.1
    if x < -text_surface.get_width():   # 文字消失在左边后，从窗口右侧重新开始
        x = 640 - text_surface.get_width()

    screen.blit(text_surface, (x, y))

    pygame.display.update()
