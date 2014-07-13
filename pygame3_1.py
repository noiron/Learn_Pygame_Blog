# -*- coding:utf8 -*-
 
# 本文件代码来自目光博客《用Python和Pygame写游戏-从入门到精通（3）》
# Pygame 的屏幕显示
# http://eyehere.net/2011/python-pygame-novice-professional-3/

# 程序功能：默认在窗口模式下显示图片，按“f”键，显示模式会在窗口和全屏之间切换

background_image_filename = 'sushiplate.jpg'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
background = pygame.image.load(background_image_filename).convert()

Fullscreen = False

while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		if event.type == KEYDOWN:
			if event.key == K_f:
				Fullscreen = not Fullscreen
				if Fullscreen:
					screen = pygame.display.set_mode((640, 480), FULLSCREEN, 32)
				else:
					screen = pygame.display.set_mode((640, 480), 0, 32)

	screen.blit(background, (0, 0))
	pygame.display.update()