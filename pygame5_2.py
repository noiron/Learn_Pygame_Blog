# -*- coding:utf8 -*-
 
# 本文件代码来自目光博客《用Python和Pygame写游戏-从入门到精通（5）》
# 像素和颜色
# http://eyehere.net/2011/python-pygame-novice-professional-5/

# 程序功能：

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

def create_scales(height):
	red_scale_surface = pygame.surface.Surface((640, height))
	green_scale_surface = pygame.surface.Surface((640, height))
	blue_scale_surface = pygame.surface.Surface((640, height))
	for x in range(640):
		c = int((x / 640.) * 255.)
		red = (c, 0, 0)
		green = (0, c, 0)
		blue = (0, 0, c)
		line_rect = Rect(x, 0, 1, height)
		pygame.draw.rect(red_scale_surface, red, line_rect)
		pygame.draw.rect(green_scale_surface, green, line_rect)
		pygame.draw.rect(blue_scale_surface, blue, line_rect)
	return red_scale_surface, green_scale_surface, blue_scale_surface

red_scale, green_scale, blue_scale = create_scales(80)

color = [127, 127, 127]

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

	screen.fill((0, 0, 0))

	screen.blit()



