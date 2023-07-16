import pygame
import random

imgEnemVerde = [pygame.image.load('imagenes/enemigoVerde.png'),pygame.image.load('imagenes/enemigoVerde1.png'),pygame.image.load('imagenes/enemigoVerde2.png')]

#Enemigo verde, sin movimiento lateral pero con disparo
enemigosVerdes = []

class EnemigoVerde:
    def __init__(self,posX,posY):
        #Cargar la imagen del enemigo azul aleatoriamente
        self.image = imgEnemVerde[random.randint(0,2)]

        #posicion y medidas
        self.x = posX
        self.y = posY
        self.ancho = self.image.get_width()
        self.alto = self.image.get_height()

        #velocidad del enemigo
        self.velocidadY = 2

        #Control del cambio de direccion
        self.contador = 0
        self.disparo = 70
    
    def dibujar(self, screen):
        """Dibuja la imagen del enemigoAzul en su posición actual en la pantalla."""
        screen.blit(self.image, (self.x, self.y))

    def actualizar(self):
        #Actualizar la logica del enemigo Azul
        self.y += self.velocidadY
        self.contador += 1
        #Realiza un disparo cada cierto tiempo
        if(self.contador > self.disparo):
            self.contador = 0
        