import pygame
import sys

from fondo import Fondo
from jugador import Jugador
from enemigoNegro import EnemigoNegro
from enemigoAzul import EnemigoAzul
from enemigoVerde import EnemigoVerde
from enemigoRojo import EnemigoRojo
from disparoJugador import DisparoJugador, disparosJugador
from disparoEnemigo import DisparoEnemigo, disparosEnemigos
from meteoritoP import MeteoritoP
from meteoritoG import MeteoritoG

#Crear el fondo
fondo = Fondo()

#Creamos el jugador
jugador = Jugador()

enemigo = EnemigoVerde(300,0)

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
    for disparo in disparosJugador:
        disparo.actualizar()
    enemigo.actualizar()
    for disparo in disparosEnemigos:
        disparo.actualizar()

    # Limpia la pantalla (pinta todo de negro)
    screen.fill((0, 0, 0))

    # Aquí iría el código de dibujo (dibujar las naves, los disparos, etc.)
    fondo.dibujar(screen)
    jugador.dibujar(screen)
    for disparo in disparosJugador:
        disparo.dibujar(screen)
    enemigo.dibujar(screen)
    for disparo in disparosEnemigos:
        disparo.dibujar(screen)

    # Actualiza la pantalla
    pygame.display.flip()
