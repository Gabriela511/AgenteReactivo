import pygame
from pygame.locals import *
from random import randint, uniform, random
from numpy import *
import sys
import time
import os

# -----------
# Constantes
# -----------

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 540
IMG_DIR = "Imagenes"

# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------

def load_image(nombre, dir_imagen, alpha=False):
    # Encontramos la ruta completa de la imagen
    ruta = os.path.join(dir_imagen, nombre)
    try:
        image = pygame.image.load(ruta)
    except:
        print("Error, no se puede cargar la imagen: " + ruta)
        sys.exit(1)
    # Comprobar si la imagen tiene "canal alpha" (como los png)
    if alpha is True:
        image = image.convert_alpha()
    else:
        image = image.convert()
    return image


class Gato(pygame.sprite.Sprite):
    "El gato y su comportamiento en la pantalla"

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("gato.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.centery = SCREEN_HEIGHT / 2
        self.posicion = [0,0]

    def update(self, po):
        if po == 1:
            self.posicion[0] = self.posicion[0] - 60
        elif po == 2:
            self.posicion[1] = self.posicion[1] - 60
        elif po == 3:
            self.posicion[0] = self.posicion[0] + 60
        else:
            self.posicion[1] = self.posicion[1] + 60

        if self.posicion[0] < 0:
            self.posicion[0] = 660

        if self.posicion[0] > 660:
            self.posicion[0] = 0

        if self.posicion[1] < 0:
            self.posicion[1] = 480

        if self.posicion[1] > 480:
            self.posicion[1] = 0

    def regresa(self, po):
        if po == 1:
            self.posicion[0] = self.posicion[0] + 60
        elif po == 2:
            self.posicion[1] = self.posicion[1] + 60
        elif po == 3:
            self.posicion[0] = self.posicion[0] - 60
        else:
            self.posicion[1] = self.posicion[1] - 60
        


class Raton(pygame.sprite.Sprite):
    "El raton y su comportamiento en la pantalla"

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("raton.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.centery = SCREEN_HEIGHT / 2


# ------------------------------
# Funcion principal del juego
# ------------------------------


def main():
    pygame.init()
    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Agente Reactivo")

    # cargamos el fondo y una imagen (se crea objetos "Surface")
    fondo = load_image("fondo.jpg", IMG_DIR, alpha = False)
    casa = pygame.image.load("Imagenes/caja.png").convert_alpha()
    perro = pygame.image.load("Imagenes/perro.png").convert_alpha()
    gato = Gato()
    raton = Raton()
    x = 0

    tux_pos_x = randint(0, 10) * 60
    tux_pos_y = randint(0, 8) * 60
    casa_pos_x = tux_pos_x
    casa_pos_y = tux_pos_y
    raton_pos_x=randint(0, 10)
    raton_pos_y=randint(0, 8)

    ratones = randint(1, 5)
    perros = randint(10, 20)
    conteo = ratones

    obstaculos_pos_x = zeros(perros)
    obstaculos_pos_y = zeros(perros)

    arreglo_pos_x = zeros(ratones)
    arreglo_pos_y = zeros(ratones)

    i = 0

    for i in range(0, ratones):

#        while arreglo_pos_x[i] != casa_pos_x and arreglo_pos_y[i] != casa_pos_y:
        arreglo_pos_x[i] = randint(0, 10) * 60
        arreglo_pos_y[i] = randint(0, 8) * 60

        i += 1


    i = 0
    for i in range(0, perros):

#        while arreglo_pos_x[i] != casa_pos_x and arreglo_pos_y[i] != casa_pos_y:
        obstaculos_pos_x[i] = randint(0, 10) * 60
        obstaculos_pos_y[i] = randint(0, 8) * 60
        if obstaculos_pos_y[i] == casa_pos_y and obstaculos_pos_x[i] == casa_pos_x:
            obstaculos_pos_x[i] = randint(0, 10) * 60
            obstaculos_pos_y[i] = randint(0, 8) * 60

        i += 1

    raton_pos_x = raton_pos_x * 60
    raton_pos_y = raton_pos_y * 60
    # Indicamos la posicion de las "Surface" sobre la ventana
    screen.blit(fondo, (0, 0))
    screen.blit(gato.image, (tux_pos_x, tux_pos_y))
    screen.blit(casa, (casa_pos_x, casa_pos_y))
    screen.blit(raton.image, (0,0))
    screen.blit(perro, (0,0))
    # se muestran lo cambios en pantalla
    pygame.display.flip()

    # el bucle principal del juego
    while conteo > 0:
        
        # le restamos 1 a la coordenada x de tux
        # asi se mueve un poquito a la izquierda
        p = randint(1,4)

        ob = 0

        if x == 0:
            if p == 1:
                tux_pos_x = tux_pos_x - 60
            elif p == 2:
               tux_pos_y = tux_pos_y - 60
            elif p == 3:
                tux_pos_x = tux_pos_x + 60
            else:
                tux_pos_y = tux_pos_y + 60

            if tux_pos_x < 0:
                tux_pos_x = 660

            if tux_pos_x > 660:
                tux_pos_x = 0

            if tux_pos_y < 0:
                tux_pos_y = 480

            if tux_pos_y > 480:
                tux_pos_y = 0

            gato.update(p)

            co = 1

            while co != 0:
                r = 0
                for r in range(0, perros):
                    if gato.posicion[0] == obstaculos_pos_x[r] and gato.posicion[1] == obstaculos_pos_y[r] or gato.posicion[0] == obstaculos_pos_x[r] and gato.posicion[1] == obstaculos_pos_y[r] or gato.posicion[1] == obstaculos_pos_y[r] and gato.posicion[0] == obstaculos_pos_x[r] or gato.posicion[1] == obstaculos_pos_y[r] and gato.posicion[0] == obstaculos_pos_x[r]:
                        gato.regresa(p)
                        p = randint(1,4)
                        gato.update(p)
                        co = 1
                        break
                    else:
                        co = 0

            r = 0
            for r in range(0, ratones):
                if gato.posicion[0] - 60 == arreglo_pos_x[r] and gato.posicion[1] == arreglo_pos_y[r] or gato.posicion[0] + 60 == arreglo_pos_x[r] and gato.posicion[1] == arreglo_pos_y[r] or gato.posicion[1] - 60 == arreglo_pos_y[r] and gato.posicion[0] == arreglo_pos_x[r] or gato.posicion[1] + 60 == arreglo_pos_y[r] and gato.posicion[0] == arreglo_pos_x[r]:
                    arreglo_pos_x[r] = -60
                    arreglo_pos_y[r] = -60
                    x = 1
                    break


        else:
            if gato.posicion[0] != casa_pos_x and ob == 0:
                if gato.posicion[0] > casa_pos_x:
                    gato.posicion[0] -= 60
                    co = 1

                    while co != 0:
                        r = 0
                        for r in range(0, perros):
                            if gato.posicion[0] == obstaculos_pos_x[r] and gato.posicion[1] == obstaculos_pos_y[r] or gato.posicion[0] == obstaculos_pos_x[r] and gato.posicion[1] == obstaculos_pos_y[r] or gato.posicion[1] == obstaculos_pos_y[r] and gato.posicion[0] == obstaculos_pos_x[r] or gato.posicion[1] == obstaculos_pos_y[r] and gato.posicion[0] == obstaculos_pos_x[r]:
                                gato.regresa(1)
                                p = randint(1,4)
                                gato.update(p)
                                ob = 1
                                co = 1
                                break
                            else:
                                co = 0
                                ob = 0
                else:
                    gato.posicion[0] += 60
                    co = 1

                    while co != 0:
                        r = 0
                        for r in range(0, perros):
                            if gato.posicion[0] == obstaculos_pos_x[r] and gato.posicion[1] == obstaculos_pos_y[r] or gato.posicion[0] == obstaculos_pos_x[r] and gato.posicion[1] == obstaculos_pos_y[r] or gato.posicion[1] == obstaculos_pos_y[r] and gato.posicion[0] == obstaculos_pos_x[r] or gato.posicion[1] == obstaculos_pos_y[r] and gato.posicion[0] == obstaculos_pos_x[r]:
                                gato.regresa(3)
                                p = randint(1,4)
                                gato.update(p)
                                ob = 1
                                co = 1
                                break
                            else:
                                ob = 0
                                co = 0

            elif gato.posicion[1] != casa_pos_y:
                if gato.posicion[1] > casa_pos_y:
                    gato.posicion[1] -= 60
                    co = 1

                    while co != 0:
                        r = 0
                        for r in range(0, perros):
                            if gato.posicion[0] == obstaculos_pos_x[r] and gato.posicion[1] == obstaculos_pos_y[r] or gato.posicion[0] == obstaculos_pos_x[r] and gato.posicion[1] == obstaculos_pos_y[r] or gato.posicion[1] == obstaculos_pos_y[r] and gato.posicion[0] == obstaculos_pos_x[r] or gato.posicion[1] == obstaculos_pos_y[r] and gato.posicion[0] == obstaculos_pos_x[r]:
                                gato.regresa(2)
                                p = randint(1,4)
                                gato.update(p)
                                ob = 1
                                co = 1
                                break
                            else:
                                ob = 0
                                co = 0
                else:
                    gato.posicion[1] += 60
                    co = 1

                    while co != 0:
                        r = 0
                        for r in range(0, perros):
                            if gato.posicion[0] == obstaculos_pos_x[r] and gato.posicion[1] == obstaculos_pos_y[r] or gato.posicion[0] == obstaculos_pos_x[r] and gato.posicion[1] == obstaculos_pos_y[r] or gato.posicion[1] == obstaculos_pos_y[r] and gato.posicion[0] == obstaculos_pos_x[r] or gato.posicion[1] == obstaculos_pos_y[r] and gato.posicion[0] == obstaculos_pos_x[r]:
                                gato.regresa(4)
                                p = randint(1,4)
                                gato.update(p)
                                co = 1
                                ob = 1
                                break
                            else:  
                                co = 0
                                ob = 0

            if gato.posicion[1] == casa_pos_y and gato.posicion[0] == casa_pos_x:
                x = 0
                conteo -= 1

        screen.blit(fondo,(0,0))
        screen.blit(gato.image, gato.posicion)
        screen.blit(casa, (casa_pos_x, casa_pos_y))


        i = 0
            
        for i in range(0, ratones):
            screen.blit(raton.image, (arreglo_pos_x[i], arreglo_pos_y[i]))
            i += 1

        i = 0
            
        for i in range(0, perros):
            screen.blit(perro, (obstaculos_pos_x[i], obstaculos_pos_y[i]))
            i += 1

        # se muestran lo cambios en pantalla
        pygame.display.flip()

        time.sleep(0.5)

        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    main()