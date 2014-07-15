# -*- coding:utf8 -*-
 
# 本文件代码来自目光博客《用Python和Pygame写游戏-从入门到精通（9）》
# 向量基础
# http://eyehere.net/2011/python-pygame-novice-professional-8/

# 程序功能：自己定义了一个向量类，以及使用gameobjects中的向量的使用实例


# # 以下为自己定义的一个向量类
# class Vector2(object):
#     def __init__(self, x=0.0, y=0.0):
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return "(%s, %s)"%(self.x, self.y)

#     @classmethod
#     def from_points(cls, P1, P2):
#         return cls( P2[0] - P1[0], P2[1] - P1[1] )

#     def get_magnitude(self):
#         return math.sqrt( self.x**2 + self.y**2 )

#     def normalize(self):
#         magnitude = self.get_magnitude()
#         self.x /= magnitude
#         self.y /= magnitude

#     def __add__(self, rhs):
#         return Vector2(self.x + rhs.x, self.y + rhs.y)
#     def __sub__(self, rhs):
#         return Vector2(self.x - rhs.x, self.y - rhs.y)

#     def __mul__(self, scalar):
#         return Vector2(self.x * scalar, self.y * scalar)
#     def __div__(self, scalar):
#         return Vector2(self.x / scalar, self.y * scalar)


# A = (10.0, 20.0)
# B = (30.0, 35.0)
# AB = Vector2.from_points(A, B)
# print AB

from gameobjects.vector2 import *
A = (10.0, 20.0)
B = (30.0, 35.0)
AB = Vector2.from_points(A, B)
print "Vector AB is", AB
print "AB * 2 is", AB * 2
print "AB / 2 is", AB / 2
print "AB + (-10, 5) is", AB + (-10, 5)
print "Magnitude of AB is", AB.get_magnitude()
print "AB normalized is", AB.get_normalized()


