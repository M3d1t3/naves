import pygame
import sys

# Inicializa Pygame
pygame.init()

# Configura el reloj para controlar el framerate
clock = pygame.time.Clock()

# Establece las dimensiones de la ventana
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Bucle principal del juego
while True:
    # Asegura que el juego se ejecuta a 60 FPS
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Aquí iría el código de actualización del juego (movimiento de las naves, disparos, etc.)

    # Limpia la pantalla (pinta todo de negro)
    screen.fill((0, 0, 0))

    # Aquí iría el código de dibujo (dibujar las naves, los disparos, etc.)

    # Actualiza la pantalla
    pygame.display.flip()
