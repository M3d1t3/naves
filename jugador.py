import pygame
from disparoJugador import DisparoJugador, disparosJugador



class Jugador:
    def __init__(self):
        # Carga la imagen del jugador
        self.image = pygame.image.load('imagenes/jugador.png')

        # Posición inicial del jugador
        self.x = 100
        self.y = 600
        self.ancho = self.image.get_width()
        self.alto = self.image.get_height()

        #Control del disparo y su retardo
        self.retardo = 10
        self.contadorRetardo = 0

        # Velocidad inicial del jugador
        self.speed = 5

    def handle_keys(self):
        """Reconoce los eventos de teclado y actualiza las variables de posición del jugador."""
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]: # Mover a la izquierda
            self.x -= self.speed
            if self.x < 0:
                self.x = 0
        if key[pygame.K_RIGHT]: # Mover a la derecha
            self.x += self.speed
            if self.x + self.ancho > 1000:
                self.x = 1000 - self.ancho
        if key[pygame.K_UP]: # Mover hacia arriba
            self.y -= self.speed
            if self.y < 0:
                self.y = 0
        if key[pygame.K_DOWN]: # Mover hacia abajo
            self.y += self.speed
            if self.y + self.alto > 800:
                self.y = 800 - self.alto
        
        #Control de la tecla de disparo
        if key[pygame.K_SPACE]:
            if self.contadorRetardo > self.retardo:
                self.contadorRetardo = 0
                self.crearDisparo()

    def dibujar(self, screen):
        """Dibuja la imagen del jugador en su posición actual en la pantalla."""
        screen.blit(self.image, (self.x, self.y))

    def actualizar(self):
        """Actualiza el estado del jugador. Esto debería llamarse una vez por frame."""
        self.handle_keys()

        #Actualizar el contador de retardo de disparo
        self.contadorRetardo += 1
 
    def crearDisparo(self):
        #Crea un nuevo disparo en la lista disparosJugador
        self.disX = self.x + (self.ancho/2) - 7
        self.disY = self.y - 20
        disparosJugador.append(DisparoJugador(self.disX,self.disY))



jugador = Jugador()