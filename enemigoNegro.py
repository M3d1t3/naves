import pygame
import random

imgEnemNegro = [pygame.image.load('imagenes/enemigoNegro.png'),pygame.image.load('imagenes/enemigoNegro1.png'),pygame.image.load('imagenes/enemigoNegro2.png')]

#Enemigo básico sin movimiento lateral ni disparo
enemigosNegros = []


class EnemigoNegro:
    def __init__(self,posX,posY):
        #Cargar la imagen del enemigo negro aleatoriamente
        self.image = imgEnemNegro[random.randint(0,2)]

        #posicion y medidas
        self.x = posX
        self.y = posY
        self.ancho = self.image.get_width()
        self.alto = self.image.get_height()

        #velocidad del enemigo
        self.velocidad = 1
    
    def dibujar(self, screen):
        """Dibuja la imagen del enemigoNegro en su posición actual en la pantalla."""
        screen.blit(self.image, (self.x, self.y))

    def actualizar(self):
        #Actualizar la logica del enemigo negro
        self.y += self.velocidad