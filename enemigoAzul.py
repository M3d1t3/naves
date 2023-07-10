import pygame
import random

imgEnemAzul = [pygame.image.load('imagenes/enemigoAzul.png'),pygame.image.load('imagenes/enemigoAzul1.png'),pygame.image.load('imagenes/enemigoAzul2.png')]


class EnemigoAzul:
    def __init__(self,posX,posY):
        #Cargar la imagen del enemigo azul aleatoriamente
        self.image = imgEnemAzul[random.randint(0,2)]

        #posicion y medidas
        self.x = posX
        self.y = posY
        self.ancho = self.image.get_width()
        self.alto = self.image.get_height()

        #velocidad del enemigo
        self.velocidadY = 2
        self.velocidadX = 2

        #Control del cambio de direccion
        self.contador = 0
        self.girar = 100
    
    def dibujar(self, screen):
        """Dibuja la imagen del enemigoAzul en su posición actual en la pantalla."""
        screen.blit(self.image, (self.x, self.y))

    def actualizar(self):
        #Actualizar la logica del enemigo Azul
        self.y += self.velocidadY
        self.x += self.velocidadX
        self.contador += 1
        if(self.contador > self.girar):
            self.contador = 0
            self.velocidadX *= -1
        