# -*-coding:utf8 -*- 
  
# 本文件代码来自目光博客《用Python和Pygame写游戏-从入门到精通（1）》 
# http://eyehere.net/2011/python-pygame-novice-professional-1/ 
  
  
background_image_filename = 'sushiplate.jpg'
mouse_image_filename = 'fugu.png'
  
# 导入pygame库 
import pygame 
# 导入一些常用的函数和常量 
from pygame.locals import *
# 向sys模块借一个exit函数用来退出程序 
from sys import exit 
  
pygame.init() 
  
screen = pygame.display.set_mode((640, 480), 0, 32) 
  
pygame.display.set_caption("Hello, World!") 
  
# 加载并转换图像 
background = pygame.image.load(background_image_filename).convert() 
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha() 
  
while True: 
    for event in pygame.event.get() 
        if event.type == QUIT: 
            exit()

    screen.blit(background, (0, 0))

    x, y = pygame.mouse.get_pos()

    x -= mouse_cursor.get_width()/2
    y -= mouse_cursor.get_height()/2

    screen.blit(mouse_cursor, (x, y))

    pygame.display.update()