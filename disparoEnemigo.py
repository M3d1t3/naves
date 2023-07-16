import pygame

#lista de disparos de los enemigos
disparosEnemigos = []

class DisparoEnemigo:
    def __init__(self, posX, posY):
        #Cargar la imagen del disparo del enemigo
        self.image = pygame.image.load('imagenes/disparoEnemigo.png')

        #posicion y medidas
        self.x = posX
        self.y = posY
        self.ancho = self.image.get_width()
        self.alto = self.image.get_height()

        #velocidad del disparo
        self.velocidad = 12

    def dibujar(self, screen):
        #Dibujar la imagen en la pantalla
        screen.blit(self.image, (self.x,self.y))
    
    def actualizar(self):
        #Actualizar la posicion
        self.y += self.velocidad
