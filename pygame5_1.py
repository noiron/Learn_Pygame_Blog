# -*- coding:utf8 -*-
 
# 本文件代码来自目光博客《用Python和Pygame写游戏-从入门到精通（5）》
# 像素和颜色
# http://eyehere.net/2011/python-pygame-novice-professional-5/

# 程序功能：画出所有的RGB颜色的组合，保存在一张图片中

import pygame
pygame.init()

# screen = pygame.display.set_mode((640, 480))

all_colors = pygame.Surface((4096, 4096), depth = 24)

# 一共会生成16*16个小区块，每个区块大小为256*256
# 将按照从左到右，从上到下的顺序依次画出每一个区块
for r in xrange(256):
	print r+1, "out of 256"		# 输出现在正在画的区块的序号
	# 确定每个区块起始处的坐标
	x = (r & 15) * 256		# x是按照0、1、2、3……14、15的循环来取值的
	y = (r >> 4) * 256		# 每画完一行的16个格子，y的值增加一个256
	for g in xrange(256):
		for b in xrange(256):
			all_colors.set_at((x+g, y+b), (r, g, b))

pygame.image.save(all_colors, "allcolors.bmp")