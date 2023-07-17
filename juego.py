import pygame
from disparoEnemigo import DisparoEnemigo, disparosEnemigos
from disparoJugador import DisparoJugador, disparosJugador
from enemigoAzul import EnemigoAzul, enemigosAzules
from enemigoNegro import EnemigoNegro, enemigosNegros
from enemigoRojo import EnemigoRojo, enemigosRojos
from enemigoVerde import EnemigoVerde, enemigosVerdes
from jugador import Jugador, jugador

#Eventos de creacion de enemigos y  meteoritos
evento1 = [{"tiempo" : 30, "tipo" : "negro", "x" : 50, "y" : -50, "creado" : 0},{"tiempo" : 30, "tipo" : "negro", "x" : 200, "y" : -50, "creado" : 0},{"tiempo" : 30, "tipo" : "negro", "x" : 350, "y" : -50, "creado" : 0},
           {"tiempo" : 30, "tipo" : "negro", "x" : 500, "y" : -50, "creado" : 0},{"tiempo" : 30, "tipo" : "negro", "x" : 650, "y" : -50, "creado" : 0},{"tiempo" : 30, "tipo" : "negro", "x" : 800, "y" : -50, "creado" : 0},
           {"tiempo" : 300, "tipo" : "negro", "x" : 50, "y" : -50, "creado" : 0},{"tiempo" : 300, "tipo" : "negro", "x" : 200, "y" : -50, "creado" : 0},{"tiempo" : 300, "tipo" : "negro", "x" : 350, "y" : -50, "creado" : 0},
           {"tiempo" : 300, "tipo" : "negro", "x" : 500, "y" : -50, "creado" : 0},{"tiempo" : 300, "tipo" : "negro", "x" : 650, "y" : -50, "creado" : 0},{"tiempo" : 300, "tipo" : "negro", "x" : 800, "y" : -50, "creado" : 0}]


#Control del juego: Creacion de enemigos, colisiones y destruccion de enemigos y disparos
class Juego:
    def __init__(self):
        self.estado = 1
        self.tiempo = 0
    
    def actualizar(self):
        #Actualizar todos los objetos del juego
        self.crearEnemigos()
        jugador.actualizar()
        for disparo in disparosJugador:
            disparo.actualizar()
        for enemigo in enemigosNegros:
            enemigo.actualizar()
        
    def dibujar(self,screen):
        #dibujar los objetos del juego
        jugador.dibujar(screen)
        for disparo in disparosJugador:
            disparo.dibujar(screen)
        for enemigo in enemigosNegros:
            enemigo.dibujar(screen)

    def crearEnemigos(self):
        #Crear enemigos comprobando los datos
        self.tiempo += 1
        if self.estado == 1:
            for evento in evento1:
                if evento["tiempo"] < self.tiempo:
                    if evento["creado"] == 0:
                        #Creamos el enemigo
                        if evento["tipo"] == "negro":
                            #Creamos un enemigo negro
                            enemigosNegros.append(EnemigoNegro(evento["x"],evento["y"]))
                            evento["creado"] = 1
                        if evento["tipo"] == "azul":
                            #creamos el enemigo azul
                            enemigosAzules.append(EnemigoAzul(evento["x"],evento["y"]))
                            evento["creado"] = 1
                        if evento["tipo"] == "verde":
                            #creamos el enemigo verde
                            enemigosVerdes.append(EnemigoVerde(evento["x"],evento["y"]))
                            evento["creado"] = 1
                        if evento["tipo"] == "rojo":
                            #creamos el enemigo rojo
                            enemigosRojos.append(EnemigoRojo(evento["x"],evento["y"]))
                            evento["creado"] = 1
