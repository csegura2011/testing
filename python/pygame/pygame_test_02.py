#!/usr/local/bin
# -*- coding: utf-8 -*-

# Referencias
# - Tutorial II Pygame: http://razonartificial.com/2010/02/pygame-2-creando-una-ventana/


import sys
import pygame
from pygame.locals import *
from pygame import *


# Modulos


# Constantes
WIDTH = 640
HEIGHT = 480


# Clases


# Funciones

def load_image(filename, transparent=False):
    try:
        image = pygame.image.load(filename)
    except pygame.error, message:
        raise SystemExit, message
    image = image.convert()
    if transparent:
        color = image.get_at((0,0))
        image.set_colorkey(color, RLEACCEL)
    return image

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pruebas Pygame")
    background_image = load('background.bmp')


    # Game Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        screen.blit(background_image,(0,0))
        pygame.display.flip()
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))
    return 0

if __name__ == "main":
    pygame.init()
    main()




