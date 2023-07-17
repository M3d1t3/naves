import pygame
import sys

from fondo import Fondo
from juego import Juego

#Crear el fondo
fondo = Fondo()

#Crear el objeto juego
juego = Juego()

# Inicializa Pygame
pygame.init()

# Configura el reloj para controlar el framerate
clock = pygame.time.Clock()

# Establece las dimensiones de la ventana
anchoPantalla = 1000
altoPantalla = 800
screen = pygame.display.set_mode((anchoPantalla, altoPantalla))

# Bucle principal del juego
while True:
    # Asegura que el juego se ejecuta a 60 FPS
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Aquí iría el código de actualización del juego (movimiento de las naves, disparos, etc.)
    juego.actualizar()

    # Limpia la pantalla (pinta todo de negro)
    screen.fill((0, 0, 0))

    # Aquí iría el código de dibujo (dibujar las naves, los disparos, etc.)
    fondo.dibujar(screen)
    juego.dibujar(screen)

    # Actualiza la pantalla
    pygame.display.flip()
