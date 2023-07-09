import pygame
import sys

from jugador import Jugador
from enemigoNegro import EnemigoNegro

#Creamos el jugador
jugador = Jugador()

#crear un enemigo negro de prueba
enemigo = EnemigoNegro(100,0)

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
    jugador.actualizar()
    enemigo.actualizar()

    # Limpia la pantalla (pinta todo de negro)
    screen.fill((0, 0, 0))

    # Aquí iría el código de dibujo (dibujar las naves, los disparos, etc.)
    jugador.dibujar(screen)
    enemigo.dibujar(screen)

    # Actualiza la pantalla
    pygame.display.flip()
