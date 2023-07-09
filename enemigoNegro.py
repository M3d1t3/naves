import pygame


class EnemigoNegro:
    def __init__(self,posX,posY):
        #Cargar la imagen del enemigo negro
        self.image = pygame.image.load('imagenes/enemigoNegro.png')

        #posicion y medidas
        self.x = posX
        self.y = posY
        self.ancho = 93
        self.alto = 84

        #velocidad del enemigo
        self.velocidad = 2
    
    def dibujar(self, screen):
        """Dibuja la imagen del enemigoNegro en su posición actual en la pantalla."""
        screen.blit(self.image, (self.x, self.y))

    def actualizar(self):
        #Actualizar la logica del enemigo negro
        self.y += self.velocidad