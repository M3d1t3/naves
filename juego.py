import pygame
from disparoEnemigo import DisparoEnemigo, disparosEnemigos
from disparoJugador import DisparoJugador, disparosJugador
from enemigoAzul import EnemigoAzul, enemigosAzules
from enemigoNegro import EnemigoNegro, enemigosNegros
from enemigoRojo import EnemigoRojo, enemigosRojos
from enemigoVerde import EnemigoVerde, enemigosVerdes
from jugador import Jugador, jugador

#Eventos de creacion de enemigos y  meteoritos por cada estado del juego
evento1 = [{"tiempo" : 30, "tipo" : "negro", "x" : 50, "y" : -50, "creado" : 0},{"tiempo" : 30, "tipo" : "negro", "x" : 200, "y" : -50, "creado" : 0},{"tiempo" : 30, "tipo" : "negro", "x" : 350, "y" : -50, "creado" : 0},
           {"tiempo" : 30, "tipo" : "negro", "x" : 500, "y" : -50, "creado" : 0},{"tiempo" : 30, "tipo" : "negro", "x" : 650, "y" : -50, "creado" : 0},{"tiempo" : 30, "tipo" : "negro", "x" : 800, "y" : -50, "creado" : 0},
           {"tiempo" : 300, "tipo" : "negro", "x" : 50, "y" : -50, "creado" : 0},{"tiempo" : 300, "tipo" : "negro", "x" : 200, "y" : -50, "creado" : 0},{"tiempo" : 300, "tipo" : "negro", "x" : 350, "y" : -50, "creado" : 0},
           {"tiempo" : 300, "tipo" : "negro", "x" : 500, "y" : -50, "creado" : 0},{"tiempo" : 300, "tipo" : "negro", "x" : 650, "y" : -50, "creado" : 0},{"tiempo" : 300, "tipo" : "negro", "x" : 800, "y" : -50, "creado" : 0}]
tiempoEvento1 = 1500

evento2 = [{"tiempo" : 30, "tipo" : "rojo", "x" : 50, "y" : -50, "creado" : 0},{"tiempo" : 30, "tipo" : "negro", "x" : 200, "y" : -50, "creado" : 0},{"tiempo" : 30, "tipo" : "negro", "x" : 350, "y" : -50, "creado" : 0},
           {"tiempo" : 30, "tipo" : "verde", "x" : 500, "y" : -50, "creado" : 0},{"tiempo" : 30, "tipo" : "negro", "x" : 650, "y" : -50, "creado" : 0},{"tiempo" : 30, "tipo" : "negro", "x" : 800, "y" : -50, "creado" : 0},
           {"tiempo" : 300, "tipo" : "rojo", "x" : 50, "y" : -50, "creado" : 0},{"tiempo" : 300, "tipo" : "negro", "x" : 200, "y" : -50, "creado" : 0},{"tiempo" : 300, "tipo" : "negro", "x" : 350, "y" : -50, "creado" : 0},
           {"tiempo" : 300, "tipo" : "azul", "x" : 500, "y" : -50, "creado" : 0},{"tiempo" : 300, "tipo" : "negro", "x" : 650, "y" : -50, "creado" : 0},{"tiempo" : 300, "tipo" : "negro", "x" : 800, "y" : -50, "creado" : 0}]
tiempoEvento2 = 1500

#Control del juego: Creacion de enemigos, colisiones y destruccion de enemigos y disparos
class Juego:
    def __init__(self):
        self.estado = 1
        self.tiempo = 0

    
    def actualizar(self):
        #Actualizar todos los objetos del juego
        self.crearEnemigos()
        self.comprobarColisiones()
        jugador.actualizar()
        for disparo in disparosJugador:
            disparo.actualizar()
        for disparo in disparosEnemigos:
            disparo.actualizar()
        for enemigo in enemigosNegros:
            enemigo.actualizar()
        for enemigo in enemigosVerdes:
            enemigo.actualizar()
        for enemigo in enemigosAzules:
            enemigo.actualizar()
        for enemigo in enemigosRojos:
            enemigo.actualizar()
        
    def dibujar(self,screen):
        #dibujar los objetos del juego
        jugador.dibujar(screen)
        for disparo in disparosJugador:
            disparo.dibujar(screen)
        for disparo in disparosEnemigos:
            disparo.dibujar(screen)
        for enemigo in enemigosNegros:
            enemigo.dibujar(screen)
        for enemigo in enemigosVerdes:
            enemigo.dibujar(screen)
        for enemigo in enemigosAzules:
            enemigo.dibujar(screen)
        for enemigo in enemigosRojos:
            enemigo.dibujar(screen)

    def crearEnemigos(self):
        #Crear enemigos comprobando los datos
        self.tiempo += 1
        if self.estado == 1:#Eventos del estado numero 1
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
            #Comprobar el fin del estado
            if self.tiempo > tiempoEvento1:
                self.estado = 2
                self.tiempo = 0
        if self.estado == 2:#Eventos del estado numero 2
            for evento in evento2:
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
            #Comprobar el fin del estado
            if self.tiempo > tiempoEvento2:
                self.estado = 3
                self.tiempo = 0

    def comprobarColisiones(self):
        # Comprobar colisiones entre disparos del jugador y enemigos
        for disparo in disparosJugador:
            for enemigo in enemigosNegros:
                if self.colision(disparo,enemigo):
                    disparosJugador.remove(disparo)
                    enemigosNegros.remove(enemigo)
            for enemigo in enemigosAzules:
                if self.colision(disparo,enemigo):
                    disparosJugador.remove(disparo)
                    enemigosAzules.remove(enemigo)
            for enemigo in enemigosVerdes:
                if self.colision(disparo,enemigo):
                    disparosJugador.remove(disparo)
                    enemigosVerdes.remove(enemigo)
            for enemigo in enemigosRojos:
                if self.colision(disparo,enemigo):
                    disparosJugador.remove(disparo)
                    enemigosRojos.remove(enemigo)

        # Comprobar colisiones entre disparos de los enemigos y el jugador
        for disparo in disparosEnemigos:
            if self.colision(disparo,jugador):
                disparosEnemigos.remove(disparo)
                # El jugador recibe un disparo

    def colision(self, obj1, obj2):
        if (obj1.x < obj2.x + obj2.ancho and
            obj1.x + obj1.ancho > obj2.x and
            obj1.y < obj2.y + obj2.alto and
            obj1.y + obj1.alto > obj2.y):
            # hay colision
            return True
        else:
            return False
