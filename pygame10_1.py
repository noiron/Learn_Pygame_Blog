# -*- coding:utf8 -*-
 
# 本文件代码来自目光博客《用Python和Pygame写游戏-从入门到精通（9）》
# 向量基础
# http://eyehere.net/2011/python-pygame-novice-professional-9/

# 程序功能：

background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.jpg'

import pygame
from pygame import *
from sys import exit
from gameobjects.vector2 import Vector2

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

