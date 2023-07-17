import pygame
import random
from disparoEnemigo import DisparoEnemigo, disparosEnemigos

imgEnemRojo = [pygame.image.load('imagenes/enemigoRojo.png'),pygame.image.load('imagenes/enemigoRojo1.png'),pygame.image.load('imagenes/enemigoRojo2.png')]

#Enemigo rojo, tiene movimiento lateral y además dispara
enemigosRojos = []


class EnemigoRojo:
    def __init__(self,posX,posY):
        #Cargar la imagen del enemigo azul aleatoriamente
        self.image = imgEnemRojo[random.randint(0,2)]

        #posicion y medidas
        self.x = posX
        self.y = posY
        self.ancho = self.image.get_width()
        self.alto = self.image.get_height()

        #velocidad del enemigo
        self.velocidadY = 1
        self.velocidadX = 2

        #Control del cambio de direccion
        self.contador = 0
        self.girar = 100

        #control de disparos
        self.retardo = random.randint(60, 100)
        self.contadorRetardo = 0
    
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
         #Comprobar y crear disparo
        self.contadorRetardo += 1
        if self.contadorRetardo > self.retardo:
            self.crearDisparo()
            self.contadorRetardo = 0

    #Crea un nuevo disparo en la lista disparosJugador
    def crearDisparo(self):
        self.disX = self.x + (self.ancho/2) - 7
        self.disY = self.y + self.alto - 30
        disparosEnemigos.append(DisparoEnemigo(self.disX,self.disY))