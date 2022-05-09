import os
import random
import time
import json


#TODO: Poner musica de pokemon de fondo

#TODO: Primero habra que leer el json y despues crear las clases pokemon y ataques con los valores del json que se han leido

class Pokemon:
    def __init__(self, name, heal, mana, potencia, type, ide, atacks, speed):
        self.nombre = name
        self.vida = heal
        self.mana = mana
        self.tipo = type
        self.potencia = potencia
        self.id = ide
        self.ataques = atacks
        self.velocidad = speed

    def atacar(self, pokemon2, ataque):
        # print(self.nombre + " va a realizar " + ataque.nombre + " !")
        # time.sleep(1)
        eficaz = False
        noEficaz = False
        curar = False
        potencia = ataque.potencia
        if ataque.tipo == "Ofensivo":
            if self.tipo == "Fuego" and pokemon2.tipo == "Planta":
                potencia = potencia * 1.25
                eficaz = True
            if self.tipo == "Planta" and pokemon2.tipo == "Fuego":
                potencia = potencia * 0.20
                noEficaz = True

            if self.tipo == "Agua" and pokemon2.tipo == "Fuego":
                potencia = potencia * 1.25
                eficaz = True
            if self.tipo == "Fuego" and pokemon2.tipo == "Agua":
                potencia = potencia * 0.20
                noEficaz = True

            if self.tipo == "Planta" and pokemon2.tipo == "Agua":
                potencia = potencia * 1.25
                eficaz = True
            if self.tipo == "Agua" and pokemon2.tipo == "Planta":
                potencia = potencia * 0.20
                noEficaz = True

            pokemon2.vida = pokemon2.vida - potencia
            # print(self.nombre + " ha causado " + str(ataque.potencia) + " de daño a " + pokemon2.nombre)
        if ataque.tipo == "Curativo":
            self.vida = self.vida + potencia
            curar = True
            # print(self.nombre + " se ha curado " + str(ataque.potencia) + " HP")
        self.mana = self.mana - ataque.costeMana
        return eficaz, curar, potencia, noEficaz

class Ataque:
    def __init__(self, potencia, costeMana, nombre, id, type, tipo2):
        self.potencia = potencia
        self.costeMana = costeMana
        self.nombre = nombre
        self.id = id
        self.tipo = type
        self.tipo2 = tipo2

class Partida:
    def __init__(self, star, stop, turno):
        self.start = star
        self.stop = stop
        self.turno = turno

    def menu(self): #TODO: Solucionar problema menu cuando quieres jugar otra partida
        while True:
            # os.system("clear")
            mode = ''
            print("SELECCIONAR MODO DE JUEGO:")
            print("1. Un jugador VS IA")
            print("2. Jugador VS Jugador")
            print("3. Salir")
            mode = int(input('Escoge una opcion: '))
            if mode == 1:
                self.stop = False
                pokemonJugador1, pokemonJugadorIA = self.seleccionarPokemonJugadorVSJugador()
                self.jugadorVSIA(pokemonJugador1,pokemonJugadorIA)
            elif mode == 2:
                self.stop = False
                pokemonJugador1, pokemonJugador2 = self.seleccionarPokemonJugadorVSJugador()
                self.jugadorVsJugador(pokemonJugador1,pokemonJugador2)
            elif mode == 3:
                exit()
            else:
                print("Opción invalida")

    def seleccionarPokemonJugadorVSJugador(self):
        listaAtaques = []
        ataque1 = Ataque(100, 10, "Ataque1", 1, "Ofensivo", "Fuego")
        ataque2 = Ataque(200, 20, "Ataque2", 2, "Ofensivo", "Fuego")
        ataque3 = Ataque(300, 30, "Ataque3", 3, "Ofensivo", "Fuego")
        ataque4 = Ataque(400, 40, "Ataque4", 4, "Ofensivo", "Agua")
        ataque5 = Ataque(100, 40, "Ataque5", 5, "Curativo", "none")
        listaAtaques = [ataque1, ataque2, ataque3, ataque4, ataque5]

        x = Pokemon("Charmander", 282, 100, 223, "Fuego", 1, listaAtaques, 251)
        y = Pokemon("Squirtle", 292, 100, 214,"Agua", 2, listaAtaques, 203)

        return x,y

    def jugadorVsJugador(self, x, y):
        while self.stop == False:
            self.resumenPartida(x, y)
            if x.velocidad > y.velocidad:
                eficaz1, curar1, ataquePokemon1, potencia1, noEficaz1 = self.partida(x, y)
                eficaz2, curar2, ataquePokemon2, potencia2, noEficaz2 = self.partida(y, x)

                self.resumenAtaque(x, y, ataquePokemon1, eficaz1, curar1, potencia1, noEficaz1)
                time.sleep(1)
                if self.finPartida(x, y) == True:
                    break

                self.resumenAtaque(y, x, ataquePokemon2, eficaz2, curar2, potencia2, noEficaz2)
                time.sleep(1)
                if self.finPartida(y, x) == True:
                    break
            else:
                eficaz1, curar1, ataquePokemon1, potencia1, noEficaz1 = self.partida(y, x)
                eficaz2, curar2, ataquePokemon2, potencia2, noEficaz2 = self.partida(x, y)

                self.resumenAtaque(y, x, ataquePokemon1, eficaz1, curar1, potencia1,noEficaz1)
                time.sleep(1)
                if self.finPartida(y, x) == True:
                    break

                self.resumenAtaque(x, y, ataquePokemon2, eficaz2, curar2, potencia2,noEficaz2)
                time.sleep(1)
                if self.finPartida(x, y) == True:
                    break

            self.turno = self.turno + 1

    def seleccionarPokemonJugadorVSIA(self): #TODO: hacer la funcion
        return 0

    def jugadorVSIA(self, x, y):
        while self.stop == False:
            self.resumenPartida(x, y)
            if x.velocidad > y.velocidad:
                eficaz1, curar1, ataquePokemon1, potencia1, noEficaz1 = self.partida(x, y)
                eficaz2, curar2, ataquePokemon2, potencia2, noEficaz2 = self.partidaIA(y, x)

                self.resumenAtaque(x, y, ataquePokemon1, eficaz1, curar1, potencia1, noEficaz1)
                time.sleep(1)
                if self.finPartida(x, y) == True:
                    break

                self.resumenAtaque(y, x, ataquePokemon2, eficaz2, curar2, potencia2, noEficaz2)
                time.sleep(1)
                if self.finPartida(y, x) == True:
                    break
            else:
                eficaz1, curar1, ataquePokemon1, potencia1, noEficaz1 = self.partidaIA(y, x)
                eficaz2, curar2, ataquePokemon2, potencia2, noEficaz2 = self.partida(x, y)

                self.resumenAtaque(y, x, ataquePokemon1, eficaz1, curar1, potencia1, noEficaz1)
                time.sleep(1)
                if self.finPartida(y, x) == True:
                    break

                self.resumenAtaque(x, y, ataquePokemon2, eficaz2, curar2, potencia2, noEficaz2)
                time.sleep(1)
                if self.finPartida(x, y) == True:
                    break

            self.turno = self.turno + 1


    def partida(self, pokemon1, pokemon2):
        # if self.turno%2 == 0:
        eficaz = False
        print("RONDA" + str(self.turno) + " !!")
        print("Es el turno de " + pokemon1.nombre)
        print("-Elige un movimiento-")
        for i in pokemon1.ataques:
            print(i.nombre)
        idMovimiento = input()
        for ataque in pokemon1.ataques:
            if str(ataque.id) == idMovimiento:
                eficaz, curar, potencia, noEficaz = pokemon1.atacar(pokemon2,ataque)
                return eficaz,curar, ataque, potencia, noEficaz

    def partidaIA(self, pokemonIA, pokemonJugador):
        eficaz = False
        movimientos = [1,2,3,4]
        movIA = random.choice(movimientos)

        print("RONDA" + str(self.turno) + " !!")
        print("Es el turno de " + pokemonIA.nombre)
        print(pokemonIA.nombre + " va a elegir su movimiento...")
        time.sleep(2)

        for ataque in pokemonIA.ataques:
            if ataque.id == movIA:
                eficaz, curar, potencia, noEficaz = pokemonIA.atacar(pokemonJugador, ataque)
                return eficaz,curar, ataque, potencia, noEficaz

    def resumenPartida(self,pokemon1,pokemon2): #TODO: poner waits, printear el proximo ataque, si es efectivo, si ha fallado, etc
        print(pokemon1.nombre)
        print("Vida: " + str(pokemon1.vida))
        print("Mana: " + str(pokemon1.mana))
        print("Velocidad: " + str(pokemon1.velocidad))
        print(" ")
        print(pokemon2.nombre)
        print("Vida: " + str(pokemon2.vida))
        print("Mana: " + str(pokemon2.mana))
        print("Velocidad: " + str(pokemon2.velocidad))

    def resumenAtaque(self, pokemon1, pokemon2, ataque, eficaz, curar, potencia, noEficaz):
        print(pokemon1.nombre + " va a realizar " + ataque.nombre + " !")
        if ataque.tipo == "Ofensivo":
            print(pokemon1.nombre + " ha causado " + str(potencia) + " de daño a " + pokemon2.nombre)
            if eficaz == True:
                print("Es super eficaz !!")
            if noEficaz == True:
                print("Es muy poco eficaz...")
        if ataque.tipo == "Curativo":
            if curar == True:
                print(pokemon1.nombre + " se ha curado " + str(potencia) + " HP")


    def finPartida(self,pokemon1,pokemon2):
        # if pokemon1.vida <= 0.0:
        #     print("Ganador " + pokemon2.nombre + "!!")
        #     self.stop = True
        #     return True
        if pokemon2.vida <= 0.0:
            print("Ganador " + pokemon1.nombre + "!!")
            self.stop = True
            return True


def main():
    partida = Partida(True,False,1)
    partida.menu()
    return 0


if __name__ == '__main__':
    main()
