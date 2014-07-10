# -*-coding:utf8 -*- 
  
# 本文件代码来自目光博客《用Python和Pygame写游戏-从入门到精通（1）》
# 理解游戏中的事件
# http://eyehere.net/2011/python-pygame-novice-professional-2/


import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

font = pygame.font.SysFont("arial", 16)
font_height = font.get_linesize()
event_text = []

while True:
	event = pygame.event.wait()
	event_text.append(str(event))
	