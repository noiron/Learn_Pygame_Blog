# -*- coding:utf8 -*-
 
# 本文件代码来自目光博客《用Python和Pygame写游戏-从入门到精通（9）》
# 向量基础
# http://eyehere.net/2011/python-pygame-novice-professional-9/

# 程序功能：显示小鱼不停的在鼠标周围游动

background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'

import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

position = Vector2(100.0, 100.0)    # 小鱼所在的初始位置
heading = Vector2()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, position)

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    # 参数前面加*意味着把列表或元组展开
    desitination = Vector2( *pygame.mouse.get_pos() ) \
        - Vector2( *sprite.get_size()) / 2
    # 计算鱼儿当前位置到鼠标位置的向量
    vector_to_mouse = Vector2.from_points(position, desitination)
    vector_to_mouse.normalize()

    # 这个heading可以看做是鱼的速度。在没有到达鼠标时，加速运动，超过以后则减速
    heading = heading + (vector_to_mouse * 0.5)

    position += heading * time_passed_seconds
    pygame.display.update()    


