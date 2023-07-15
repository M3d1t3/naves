import pygame

class MeteoritoG:
    def __init__(self, posX, posY):
        #Cargar la imagen del disparo del jugador
        self.image = pygame.image.load('imagenes/meteoritoGrande.png')

        #posicion y medidas
        self.x = posX
        self.y = posY
        self.ancho = self.image.get_width()
        self.alto = self.image.get_height()

        #velocidad del disparo
        self.velocidadY = 1

    def dibujar(self, screen):
        #Dibujar la imagen en la pantalla
        screen.blit(self.image, (self.x,self.y))
    
    def actualizar(self):
        #Actualizar la posicion
        self.y += self.velocidadY
 