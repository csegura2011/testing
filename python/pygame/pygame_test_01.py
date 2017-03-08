#!/usr/local/bin
# -*- coding: utf-8 -*-
#
# # Referencias
# # - http://razonartificial.com/2010/02/pygame-1-importar-inicializar/
#
#
# import pygame
# from pygame.locals import *
#
#
# # Modulos
#
#
# # Constantes
#
#
# # Clases
#
#
# # Funciones
#
#
#
#
# def main():
#     return 0
#
# if __name__ == "main":
#     pygame.init()
#     main()

import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()


