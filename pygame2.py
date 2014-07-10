# -*- coding:utf8 -*-

# 载入相应包
import pygame
from pygame.locals import *
from sys import exit

# 将pygame模块初始化
pygame.init()
SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

font = pygame.font.SysFont("arial", 16)
font_height = font.get_linesize()
event_text = []

while True:
	event = pygame.event.wait()
	event_text.append(str(event))	# 获得事件的名字
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