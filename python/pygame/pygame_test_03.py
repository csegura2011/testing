#!/usr/bin/python
# -*- coding: utf-8 -*-

# Referencias
# - http://www.pygame.org/docs/tut/PygameIntro.html


import sys
import pygame

pygame.init()

size = width, height = 640, 480
speed = [5,5]
black = 0,0,0

print type(size)

screen = pygame.display.set_mode(size)
background = pygame.image.load('background.bmp')
backgroundrect = background.get_rect()
ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(background, backgroundrect)
    screen.blit(ball, ballrect)
    pygame.display.flip()


