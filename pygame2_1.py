# -*-coding:utf8 -*- 
  
# 本文件代码来自目光博客《用Python和Pygame写游戏-从入门到精通（1）》
# 理解游戏中的事件
# http://eyehere.net/2011/python-pygame-novice-professional-2/

# 导入相应模块
import pygame
from pygame.locals import *
from sys import exit

pygame.init()   # 初始化pygame
SCREEN_SIZE = (640, 480)    # 设定窗口的大小
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)    # 设置显示窗口相应的参数

font = pygame.font.SysFont("arial", 16)     # 设置用于显示的字体及大小
font_height = font.get_linesize()   
event_text = []

while True:
    event = pygame.event.wait()
    event_text.append(str(event))   # 获得事件的名字
    event_text = event_text[-SCREEN_SIZE[1]/font_height:]

    if event.type == QUIT:
        exit()

    screen.fill((255, 255, 255))

    # 从屏幕的最下方开始输出，留一行的空
    y = SCREEN_SIZE[1] - font_height
    for text in reversed(event_text):
        screen.blit( font.render(text, True, (0, 0, 0)), (0, y) )
        y -= font_height


    pygame.display.update()

    

    