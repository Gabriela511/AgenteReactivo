#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escrito por Daniel Fuentes B.
# Licencia: X11/MIT license http://www.opensource.org/licenses/mit-license.php
# https://www.pythonmania.net/es/2010/03/25/tutorial-pygame-2-ventana-e-imagenes/

# ---------------------------
# Importacion de los módulos
# ---------------------------

import pygame
from pygame.locals import *
from random import randint, uniform, random
import sys
import time

# -----------
# Constantes
# -----------

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------


# ------------------------------
# Funcion principal del juego
# ------------------------------


def main():
    pygame.init()
    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("tutorial pygame parte 2")

    # cargamos el fondo y una imagen (se crea objetos "Surface")
    fondo = pygame.image.load("fondo.jpg").convert()
    tux = pygame.image.load("tux.png").convert_alpha()

    tux_pos_x = 550
    tux_pos_y = 200

    # Indicamos la posicion de las "Surface" sobre la ventana
    screen.blit(fondo, (0, 0))
    screen.blit(tux, (0, 0))
    # se muestran lo cambios en pantalla
    pygame.display.flip()

    # el bucle principal del juego
    while True:

        # le restamos 1 a la coordenada x de tux
        # asi se mueve un poquito a la izquierda
        p = randint(1,4)

        if p == 1:
            tux_pos_x = tux_pos_x - 90
        elif p == 2:
            tux_pos_y = tux_pos_y - 90
        elif p == 3:
            tux_pos_x = tux_pos_x + 90
        else:
            tux_pos_y = tux_pos_y + 90

        if tux_pos_x < 1:
            tux_pos_x = 550

        if tux_pos_x >= 640:
            tux_pos_x = 0

        if tux_pos_y < 1:
            tux_pos_y = 390

        if tux_pos_y >= 480:
            tux_pos_y = 0

        screen.blit(fondo,(0,0))
        screen.blit(tux, (tux_pos_x, tux_pos_y))
        # se muestran lo cambios en pantalla
        pygame.display.flip()

        time.sleep(2)

        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    main()