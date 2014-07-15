# -*- coding:utf8 -*-
 
# 本文件代码来自目光博客《用Python和Pygame写游戏-从入门到精通（4）》
# 使用字体模块，Pygame 的错误处理
# http://eyehere.net/2011/python-pygame-novice-professional-4/

# 程序功能：利用选定字体将文字输出成一张图片

my_name = "Will McGugan"
import pygame
from pygame.locals import *
from sys import exit
pygame.init()
my_font = pygame.font.SysFont("arial", 64)
name_surface = my_font.render(my_name, True, (0, 0, 0), (255, 255, 255))
pygame.image.save(name_surface, "name.jpg")

# 以下部分是将文字在窗口中输出（原博客中没有）
# while True:
#     screen = pygame.display.set_mode((400, 200), 0, 32)
#     screen.blit(name_surface, (0, 0))
#     pygame.display.update()
#     event = pygame.event.wait()
#     if event.type == QUIT:
#         exit()
        
