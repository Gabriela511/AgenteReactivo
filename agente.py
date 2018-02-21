# He incluido la librería "os" para manejar directorios
import sys, os, pygame
pygame.init()

# Me sitúo en el directorio de trabajo. Descomenta y edita la que corresponda
# según tu sistema operativo
# Windows
# os.chdir("c:\prog\python34\pitando")
# Mac OS X
# os.chdir("/Users/gvisoc/pitando")
# Raspberry Pi
os.chdir("/home/pi/pitando")

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0
screen = pygame.display.set_mode(size)
ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()

# Limitamos el número de cuadros por segundo de la animación
FRAMERATE = 60
# y cargamos un reloj que usará el valor anterior
clock = pygame.time.Clock()

try:
    while 1:
        # Esperamos al siguiente "tick", a intervalos de 1 / 60 segundos.
        clock.tick(FRAMERATE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(black)
        screen.blit(ball, ballrect)
        pygame.display.flip()
except KeyboardInterrupt:
    print ("User exits")
    sys.exit()