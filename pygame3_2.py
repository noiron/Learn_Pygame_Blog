# -*- coding:utf8 -*-
 
# 本文件代码来自目光博客《用Python和Pygame写游戏-从入门到精通（3）》
# Pygame 的屏幕显示
# http://eyehere.net/2011/python-pygame-novice-professional-3/

# 程序功能：将显示窗口设置为可以调节大小的

background_image_filename = 'sushiplate.jpg'

import pygame
from pygame.locals import *
from sys import exit

SCREEN_SIZE = (640, 480)

pygame.init()
# 设定窗口的属性，可以调节大小
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
# 读取图片作为背景
background = pygame.image.load(background_image_filename).convert()

while True:

    event = pygame.event.wait()
    if event.type == QUIT:
        exit()
    # 如果事件是调整窗口大小
    if event.type == VIDEORESIZE:
        # 获得新的窗口大小
        SCREEN_SIZE = event.size
        # 下面这一句会导致程序在调整窗口时出错退出，可能与Windows系统有关
        # 解决方法：Try removing the color depth on the resize mode setting.
        # screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
        screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE)
        pygame.display.set_caption("Window resized to " + str(event.size))

    screen_width, screen_height = SCREEN_SIZE

    # 以背景图片的长和宽为步长，重新绘制窗口
    for y in range(0, screen_height, background.get_height()):
        for x in range(0, screen_width, background.get_width()):
            screen.blit(background, (x, y))

    pygame.display.update()
