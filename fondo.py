import pygame

class Fondo:
    def __init__(self):
        #Carga la imagen del fondo
        self.image = pygame.image.load("imagenes/fondo2.png")
    
    def dibujar(self,screen):
        for i in range(0, 1000, 256):     # Rango de 0 a 800 (ancho de la pantalla), incrementando en 256 en cada paso
            for j in range(0, 800, 256): # Rango de 0 a 600 (alto de la pantalla), incrementando en 256 en cada paso
                screen.blit(self.image, (i, j))