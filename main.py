import os
import random
import time
import json


#TODO: Poner musica de pokemon de fondo

#TODO: Primero habra que leer el json y despues crear las clases pokemon y ataques con los valores del json que se han leido

#TODO: Mirar error porque falta añadir tipo Dragon, Normal...


def logo():
    print("Pokemon Game inspired in Generation 1, coded by snavarrete7 (Python 3.10)")
    print("")
    print("                                      kkkkkkkk")
    print("                                      k::::::k")
    print("ppppp   ppppppppp      ooooooooooo    k:::::k    kkkkkkk    eeeeeeeeeeee       mmmmmmm    mmmmmmm      ooooooooooo   nnnn  nnnnnnnn")
    print("p::::ppp:::::::::p   oo:::::::::::oo  k:::::k   k:::::k   ee::::::::::::ee   mm:::::::m  m:::::::mm  oo:::::::::::oo n:::nn::::::::nn")
    print("p:::::::::::::::::p o:::::::::::::::o k:::::k  k:::::k   e::::::eeeee:::::eem::::::::::mm::::::::::mo:::::::::::::::on::::::::::::::nn")
    print("pp::::::ppppp::::::po:::::ooooo:::::o k:::::k k:::::k   e::::::e     e:::::em::::::::::::::::::::::mo:::::ooooo:::::onn:::::::::::::::n")
    print("p:::::p     p:::::po::::o     o::::o k::::::k:::::k    e:::::::eeeee::::::em:::::mmm::::::mmm:::::mo::::o     o::::o  n:::::nnnn:::::n")
    print("p:::::p     p:::::po::::o     o::::o k:::::::::::k     e:::::::::::::::::e m::::m   m::::m   m::::mo::::o     o::::o  n::::n    n::::n")
    print("p:::::p     p:::::po::::o     o::::o k:::::::::::k     e::::::eeeeeeeeeee  m::::m   m::::m   m::::mo::::o     o::::o  n::::n    n::::n")
    print("p:::::p    p::::::po::::o     o::::o k::::::k:::::k    e:::::::e           m::::m   m::::m   m::::mo::::o     o::::o  n::::n    n::::n")
    print("p:::::ppppp:::::::po:::::ooooo:::::ok::::::k k:::::k   e::::::::e          m::::m   m::::m   m::::mo:::::ooooo:::::o  n::::n    n::::n")
    print("p::::::::::::::::p o:::::::::::::::ok::::::k  k:::::k   e::::::::eeeeeeee  m::::m   m::::m   m::::mo:::::::::::::::o  n::::n    n::::n")
    print("p::::::::::::::pp   oo:::::::::::oo k::::::k   k:::::k   ee:::::::::::::e  m::::m   m::::m   m::::m oo:::::::::::oo   n::::n    n::::n")
    print("p::::::pppppppp       ooooooooooo   kkkkkkkk    kkkkkkk    eeeeeeeeeeeeee  mmmmmm   mmmmmm   mmmmmm   ooooooooooo     nnnnnn    nnnnnn")
    print("p:::::p")
    print("p:::::p")
    print("p:::::::p")
    print("p:::::::p")
    print("p:::::::p")
    print("ppppppppp")
    print(" ")

class Jugador:
    def __init__(self, name):
        self.nombre = name
        self.equipoPokemon = []

    def elegirEquipo(self):
        if self.nombre != "IA":
            print(self.nombre + "Selecciona los 4 pokemons de tu equipo!")
            for x in range(4):
                pokemon = self.seleccionaPokemon()
                self.equipoPokemon.append(pokemon)
        else:
            for x in range(4):
                pokemon = self.seleccionaPokemonIA()
                self.equipoPokemon.append(pokemon)


    def seleccionaPokemon(self):
        f = open("pokemon.json", "r")
        c = f.read()
        f.close()
        js = json.loads(c)

        for x in js:
            print("--------------------------------")
            print(js[x]["Nombre"])
            print("Vida: " + str(js[x]["Vida"]))
            print("Potencia: " + str(js[x]["Potencia"]))
            print("Potencia: especial " + str(js[x]["Potencia especial"]))
            print("Defensa: " + str(js[x]["Defensa"]))
            print("Defensa especial: " + str(js[x]["Defensa especial"]))
            print("Tipo: " + str(js[x]["Tipo"]))
            print("Introduce " + x + " para seleccionar a " + js[x]["Nombre"])
            print("--------------------------------")

        opcionJugador1 = input("Numero del pokemon escogido: ")

        listaAtaquesX = []
        for x in range(4):
            ataque = Ataque(js[str(opcionJugador1)]["Ataques"][0][str(x + 1)]["Potencia"],
                            js[str(opcionJugador1)]["Ataques"][0][str(x + 1)]["PP"],
                            js[str(opcionJugador1)]["Ataques"][0][str(x + 1)]["PP"],
                            js[str(opcionJugador1)]["Ataques"][0][str(x + 1)]["Nombre"],
                            js[str(opcionJugador1)]["Ataques"][0][str(x + 1)]["Id"],
                            js[str(opcionJugador1)]["Ataques"][0][str(x + 1)]["Tipo1"],
                            js[str(opcionJugador1)]["Ataques"][0][str(x + 1)]["Tipo2"],
                            js[str(opcionJugador1)]["Ataques"][0][str(x + 1)]["Especial"])
            listaAtaquesX.append(ataque)

        pokemon = Pokemon(js[str(opcionJugador1)]["Nombre"], js[str(opcionJugador1)]["Vida"],
                                  js[str(opcionJugador1)]["Mana"], js[str(opcionJugador1)]["Potencia"],
                                  js[str(opcionJugador1)]["Potencia especial"], js[str(opcionJugador1)]["Defensa"],
                                  js[str(opcionJugador1)]["Defensa especial"], js[str(opcionJugador1)]["Tipo"],
                                  js[str(opcionJugador1)]["Id"], listaAtaquesX, js[str(opcionJugador1)]["Velocidad"])

        return pokemon

    def seleccionaPokemonIA(self):
        f = open("pokemon.json", "r")
        c = f.read()
        f.close()
        js = json.loads(c)

        nElementos = 0
        for x in js:
            nElementos = nElementos + 1

        opcionJugadorIA = random.randint(1, nElementos)

        listaAtaquesX = []
        for x in range(4):
            ataque = Ataque(js[str(opcionJugadorIA)]["Ataques"][0][str(x + 1)]["Potencia"],
                            js[str(opcionJugadorIA)]["Ataques"][0][str(x + 1)]["PP"],
                            js[str(opcionJugadorIA)]["Ataques"][0][str(x + 1)]["PP"],
                            js[str(opcionJugadorIA)]["Ataques"][0][str(x + 1)]["Nombre"],
                            js[str(opcionJugadorIA)]["Ataques"][0][str(x + 1)]["Id"],
                            js[str(opcionJugadorIA)]["Ataques"][0][str(x + 1)]["Tipo1"],
                            js[str(opcionJugadorIA)]["Ataques"][0][str(x + 1)]["Tipo2"],
                            js[str(opcionJugadorIA)]["Ataques"][0][str(x + 1)]["Especial"])
            listaAtaquesX.append(ataque)

        pokemon = Pokemon(js[str(opcionJugadorIA)]["Nombre"], js[str(opcionJugadorIA)]["Vida"],
                                  js[str(opcionJugadorIA)]["Mana"], js[str(opcionJugadorIA)]["Potencia"],
                                  js[str(opcionJugadorIA)]["Potencia especial"], js[str(opcionJugadorIA)]["Defensa"],
                                  js[str(opcionJugadorIA)]["Defensa especial"], js[str(opcionJugadorIA)]["Tipo"],
                                  js[str(opcionJugadorIA)]["Id"], listaAtaquesX, js[str(opcionJugadorIA)]["Velocidad"])

        return pokemon

class Pokemon:
    def __init__(self, name, heal, mana, potencia, potenciaEspecial, defensa, defensaEspecial, type, ide, atacks, speed):
        self.nombre = name
        self.vida = heal
        self.mana = mana
        self.tipo = type
        self.potencia = potencia
        self.potenciaEspecial = potenciaEspecial
        self.defensa = defensa
        self.defensaEspecial = defensaEspecial
        self.id = ide
        self.ataques = atacks
        self.velocidad = speed

    def atacar(self, pokemon2, ataque):
        # print(self.nombre + " va a realizar " + ataque.nombre + " !")
        # time.sleep(1)

        eficaz = False
        noEficaz = False
        curar = False
        estadistico = False
        N = 100
        E = 1
        if ataque.especial == True:
            A = self.potenciaEspecial
            D = pokemon2.defensaEspecial
        else:
            A = self.potencia
            D = pokemon2.defensa
        P = ataque.potencia
        V = random.randint(85,100)

        if ataque.tipo2 == self.tipo:
            B = 1.5
        else:
            B = 1

        if ataque.tipo == "Ofensivo":
            if self.tipo == "Fuego" and pokemon2.tipo == "Planta":
                valores = [1, 2, 4]
                E = random.choice(valores)
                eficaz = True
            if self.tipo == "Planta" and pokemon2.tipo == "Fuego":
                valores = [0, 0.25, 0.5]
                E = random.choice(valores)
                noEficaz = True

            if self.tipo == "Agua" and pokemon2.tipo == "Fuego":
                valores = [1, 2, 4]
                E = random.choice(valores)
                eficaz = True
            if self.tipo == "Fuego" and pokemon2.tipo == "Agua":
                valores = [0, 0.25, 0.5]
                E = random.choice(valores)
                noEficaz = True

            if self.tipo == "Planta" and pokemon2.tipo == "Agua":
                valores = [1, 2, 4]
                E = random.choice(valores)
                eficaz = True
            if self.tipo == "Agua" and pokemon2.tipo == "Planta":
                valores = [0, 0.25, 0.5]
                E = random.choice(valores)
                noEficaz = True

            formula = 0.01 * B * E * V * ((((0.2*N+1)*A*P)/(25*D))+2)  #TODO: si la E es 0 printear un mensaje de ha falldo
            damage = round(formula)
            pokemon2.vida = pokemon2.vida - damage
            self.mana = self.mana - ataque.PP
            return eficaz, curar, damage, noEficaz, estadistico

        curacion = ataque.potencia
        if ataque.tipo == "Curativo":
            self.vida = self.vida + curacion
            curar = True
            self.mana = self.mana - ataque.PP
            return eficaz, curar, curacion, noEficaz, estadistico
        if ataque.tipo == "Estadistico":
            pokemon2.defensa = pokemon2.defensa - ataque.potencia
            pokemon2.defensaEspecial = pokemon2.defensaEspecial - ataque.potencia
            estadistico = True
            return eficaz, curar, curacion, noEficaz, estadistico

        # potencia = ataque.potencia
        # if ataque.tipo == "Ofensivo":
        #     if self.tipo == "Fuego" and pokemon2.tipo == "Planta":
        #         potencia = potencia * 1.25
        #         eficaz = True
        #     if self.tipo == "Planta" and pokemon2.tipo == "Fuego":
        #         potencia = potencia * 0.20
        #         noEficaz = True
        #
        #     if self.tipo == "Agua" and pokemon2.tipo == "Fuego":
        #         potencia = potencia * 1.25
        #         eficaz = True
        #     if self.tipo == "Fuego" and pokemon2.tipo == "Agua":
        #         potencia = potencia * 0.20
        #         noEficaz = True
        #
        #     if self.tipo == "Planta" and pokemon2.tipo == "Agua":
        #         potencia = potencia * 1.25
        #         eficaz = True
        #     if self.tipo == "Agua" and pokemon2.tipo == "Planta":
        #         potencia = potencia * 0.20
        #         noEficaz = True
        #
        #     pokemon2.vida = pokemon2.vida - potencia
        #     # print(self.nombre + " ha causado " + str(ataque.potencia) + " de daño a " + pokemon2.nombre)
        # if ataque.tipo == "Curativo":
        #     self.vida = self.vida + potencia
        #     curar = True
        #     # print(self.nombre + " se ha curado " + str(ataque.potencia) + " HP")
        # self.mana = self.mana - ataque.costeMana


class Ataque:
    def __init__(self, potencia, costeMana, PP, nombre, id, tipo1, tipo2, especial):
        self.potencia = potencia
        self.costeMana = costeMana
        self.PP = PP
        self.nombre = nombre
        self.id = id
        self.tipo = tipo1
        self.tipo2 = tipo2
        self.especial = especial

class Partida:
    def __init__(self, star, stop, turno):
        self.start = star
        self.stop = stop
        self.turno = turno

    def menu(self):
        while True:
            # os.system("clear")
            mode = ''
            print("SELECCIONAR MODO DE JUEGO:")
            print("1. Un jugador VS IA")
            print("2. Jugador VS Jugador")
            print("3. Modo Equipo")
            print("4. Salir")
            mode = int(input('Escoge una opcion: '))
            if mode == 1:
                self.stop = False
                pokemonJugador1, pokemonJugadorIA = self.seleccionarPokemonJugadorVSIA()
                self.jugadorVSIA(pokemonJugador1,pokemonJugadorIA)
            elif mode == 2:
                self.stop = False
                pokemonJugador1, pokemonJugador2 = self.seleccionarPokemonJugadorVSJugador()
                self.jugadorVsJugador(pokemonJugador1,pokemonJugador2)
            elif mode == 4:
                exit()
            elif mode == 3:
                print("1. Batalla por equipos vs IA")
                selec = int(input())
                if selec == 1:
                    print("Escribe tu nombre de usuario: ")
                    nombre = input()
                    jugador = Jugador(nombre)
                    jugadorIA = Jugador("IA")
                    self.batallaEquiposIA(jugador,jugadorIA)
            else:
                print("Opción invalida")

    def batallaEquiposIA(self, jugador1, jugadorIA):
        jugador1.elegirEquipo()
        jugadorIA.elegirEquipo()

        print("")
        print("Equipo de " + jugador1.nombre)
        for x in jugador1.equipoPokemon:
            print(x.nombre)
        print("")
        print("Equipo de " + jugadorIA.nombre)
        for x in jugadorIA.equipoPokemon:
            print(x.nombre)

        print("La batalla va a comenzar!")
        time.sleep(2)

    def seleccionarPokemonJugadorVSJugador(self):

        print("")
        print("SELECCIONA UN POKEMON: ")
        print("")

        f = open("pokemon.json", "r")
        c = f.read()
        f.close()
        js = json.loads(c)

        for x in js:
            print("--------------------------------")
            print(js[x]["Nombre"])
            print("Vida: " + str(js[x]["Vida"]))
            print("Potencia: " + str(js[x]["Potencia"]))
            print("Potencia: especial " + str(js[x]["Potencia especial"]))
            print("Defensa: " + str(js[x]["Defensa"]))
            print("Defensa especial: " + str(js[x]["Defensa especial"]))
            print("Tipo: " + str(js[x]["Tipo"]))
            print("Introduce " + x + " para seleccionar a " + js[x]["Nombre"])
            print("--------------------------------")

        opcionJugador1 = input("Numero del pokemon escogido por el JUGADOR 1: ")
        opcionJugador2 = input("Numero del pokemon escogido por el JUGADOR 2: ")

        #TODO: inicializar valores de ataques y pokemons
        #(potencia, costeMana, PP, nombre, id, tipo1, tipo2, especial)
        #(name, heal, mana, potencia, potenciaEspecial, defensa, defensaEspecial, type, ide, atacks, speed)

        listaAtaquesX = []
        for x in range(4):
            ataque = Ataque(js[str(opcionJugador1)]["Ataques"][0][str(x + 1)]["Potencia"],
                            js[str(opcionJugador1)]["Ataques"][0][str(x + 1)]["PP"],
                            js[str(opcionJugador1)]["Ataques"][0][str(x + 1)]["PP"],
                            js[str(opcionJugador1)]["Ataques"][0][str(x + 1)]["Nombre"],
                            js[str(opcionJugador1)]["Ataques"][0][str(x + 1)]["Id"],
                            js[str(opcionJugador1)]["Ataques"][0][str(x + 1)]["Tipo1"],
                            js[str(opcionJugador1)]["Ataques"][0][str(x + 1)]["Tipo2"],
                            js[str(opcionJugador1)]["Ataques"][0][str(x + 1)]["Especial"])
            listaAtaquesX.append(ataque)

        pokemonJugador1 = Pokemon(js[str(opcionJugador1)]["Nombre"], js[str(opcionJugador1)]["Vida"],
                                  js[str(opcionJugador1)]["Mana"], js[str(opcionJugador1)]["Potencia"],
                                  js[str(opcionJugador1)]["Potencia especial"], js[str(opcionJugador1)]["Defensa"],
                                  js[str(opcionJugador1)]["Defensa especial"], js[str(opcionJugador1)]["Tipo"],
                                  js[str(opcionJugador1)]["Id"], listaAtaquesX, js[str(opcionJugador1)]["Velocidad"])

        listaAtaquesY = []
        for x in range(4):
            ataque = Ataque(js[str(opcionJugador2)]["Ataques"][0][str(x + 1)]["Potencia"],
                            js[str(opcionJugador2)]["Ataques"][0][str(x + 1)]["PP"],
                            js[str(opcionJugador2)]["Ataques"][0][str(x + 1)]["PP"],
                            js[str(opcionJugador2)]["Ataques"][0][str(x + 1)]["Nombre"],
                            js[str(opcionJugador2)]["Ataques"][0][str(x + 1)]["Id"],
                            js[str(opcionJugador2)]["Ataques"][0][str(x + 1)]["Tipo1"],
                            js[str(opcionJugador2)]["Ataques"][0][str(x + 1)]["Tipo2"],
                            js[str(opcionJugador2)]["Ataques"][0][str(x + 1)]["Especial"])
            listaAtaquesY.append(ataque)

        pokemonJugador2 = Pokemon(js[str(opcionJugador2)]["Nombre"], js[str(opcionJugador2)]["Vida"],
                                  js[str(opcionJugador2)]["Mana"], js[str(opcionJugador2)]["Potencia"],
                                  js[str(opcionJugador2)]["Potencia especial"], js[str(opcionJugador2)]["Defensa"],
                                  js[str(opcionJugador2)]["Defensa especial"], js[str(opcionJugador2)]["Tipo"],
                                  js[str(opcionJugador2)]["Id"], listaAtaquesY, js[str(opcionJugador2)]["Velocidad"])

        return pokemonJugador1, pokemonJugador2

    def seleccionarPokemonPrueba(self):

        ataque1 = Ataque(120, 10, 10, "Lanazallamas", 1, "Ofensivo", "Fuego", False)
        ataque2 = Ataque(65, 15, 15,"Puño de fuego", 2, "Ofensivo", "Fuego", False)
        ataque3 = Ataque(50, 20, 20,"Bomba de humo", 3, "Estadistico", "Normal", False)
        ataque4 = Ataque(80, 20, 20,"Aliento de dragon", 4, "Ofensivo", "Fuego", True)
        listaAtaquesX = [ataque1, ataque2, ataque3, ataque4]

        ataque5 = Ataque(40, 10, 10,"Pistola agua", 1, "Ofensivo", "Agua",True)
        ataque6= Ataque(90, 10, 10,"Corte de agua", 2, "Ofensivo", "Agua",False)
        ataque7= Ataque(50, 40, 40,"Golpe rapido", 3, "Ofensivo", "Normal",False)
        ataque8= Ataque(110, 5, 5,"Hydro bomba", 4, "Ofensivo", "Agua",True)
        listaAtaquesY = [ataque5, ataque6, ataque7, ataque8]

        x = Pokemon("Charmander", 282, 1000, 223, 240, 203, 218, "Fuego", 1, listaAtaquesX, 251)
        y = Pokemon("Squirtle", 292, 1000, 214, 218, 251, 249, "Agua", 2, listaAtaquesY, 203)

        return x, y

    def jugadorVsJugador(self, x, y):
        while self.stop == False:
            self.resumenPartida(x, y)
            if x.velocidad > y.velocidad:
                eficaz1, curar1, ataquePokemon1, potencia1, noEficaz1, estad1 = self.partida(x, y)
                eficaz2, curar2, ataquePokemon2, potencia2, noEficaz2, estad2 = self.partida(y, x)

                self.resumenAtaque(x, y, ataquePokemon1, eficaz1, curar1, potencia1, noEficaz1, estad1)
                time.sleep(2)
                if self.finPartida(x, y) == True:
                    break

                self.resumenAtaque(y, x, ataquePokemon2, eficaz2, curar2, potencia2, noEficaz2, estad2)
                time.sleep(2)
                if self.finPartida(y, x) == True:
                    break
            else:
                eficaz1, curar1, ataquePokemon1, potencia1, noEficaz1, estad1 = self.partida(y, x)
                eficaz2, curar2, ataquePokemon2, potencia2, noEficaz2, estad2 = self.partida(x, y)

                self.resumenAtaque(y, x, ataquePokemon1, eficaz1, curar1, potencia1,noEficaz1, estad1)
                time.sleep(2)
                if self.finPartida(y, x) == True:
                    break

                self.resumenAtaque(x, y, ataquePokemon2, eficaz2, curar2, potencia2,noEficaz2, estad2)
                time.sleep(2)
                if self.finPartida(x, y) == True:
                    break

            self.turno = self.turno + 1


    def jugadorVSIA(self, x, y):
        while self.stop == False:
            self.resumenPartida(x, y)
            if x.velocidad > y.velocidad:
                eficaz1, curar1, ataquePokemon1, potencia1, noEficaz1, estad1 = self.partida(x, y)
                eficaz2, curar2, ataquePokemon2, potencia2, noEficaz2, estad2 = self.partidaIA(y, x)

                self.resumenAtaque(x, y, ataquePokemon1, eficaz1, curar1, potencia1, noEficaz1, estad1)
                time.sleep(2)
                if self.finPartida(x, y) == True:
                    break

                self.resumenAtaque(y, x, ataquePokemon2, eficaz2, curar2, potencia2, noEficaz2, estad2)
                time.sleep(2)
                if self.finPartida(y, x) == True:
                    break
            else:
                eficaz1, curar1, ataquePokemon1, potencia1, noEficaz1, estad1 = self.partidaIA(y, x)
                eficaz2, curar2, ataquePokemon2, potencia2, noEficaz2, estad2 = self.partida(x, y)

                self.resumenAtaque(y, x, ataquePokemon1, eficaz1, curar1, potencia1, noEficaz1, estad1)
                time.sleep(2)
                if self.finPartida(y, x) == True:
                    break

                self.resumenAtaque(x, y, ataquePokemon2, eficaz2, curar2, potencia2, noEficaz2, estad2)
                time.sleep(2)
                if self.finPartida(x, y) == True:
                    break

            self.turno = self.turno + 1

    def seleccionarPokemonJugadorVSIA(self):

        print("")
        print("SELECCIONA UN POKEMON: ")
        print("")

        f = open("pokemon.json", "r")
        c = f.read()
        f.close()
        js = json.loads(c)
        nElementos = 0
        for x in js:
            print("--------------------------------")
            print(js[x]["Nombre"])
            print("Vida: " + str(js[x]["Vida"]))
            print("Potencia: " + str(js[x]["Potencia"]))
            print("Potencia especial: " + str(js[x]["Potencia especial"]))
            print("Defensa: " + str(js[x]["Defensa"]))
            print("Defensa: especial " + str(js[x]["Defensa especial"]))
            print("Tipo: " + str(js[x]["Tipo"]))
            print("Introduce " + x + " para seleccionar a " + js[x]["Nombre"])
            print("--------------------------------")

        for elemento in js:
            nElementos = nElementos + 1

        opcionJugador1 = input("Numero del pokemon escogido por el JUGADOR 1: ")
        opcionIA = str(random.randint(1, nElementos))

        while True:
            if opcionIA == opcionJugador1:
                opcionIA = str(random.randint(1, nElementos))
            else:
                break

        # TODO: inicializar valores de ataques y pokemons
        # (potencia, costeMana, PP, nombre, id, tipo1, tipo2, especial)
        # (name, heal, mana, potencia, potenciaEspecial, defensa, defensaEspecial, type, ide, atacks, speed)

        listaAtaquesX = []
        for x in range(4):
            ataque = Ataque(js[str(opcionJugador1)]["Ataques"][0][str(x + 1)]["Potencia"],
                            js[str(opcionJugador1)]["Ataques"][0][str(x + 1)]["PP"],
                            js[str(opcionJugador1)]["Ataques"][0][str(x + 1)]["PP"],
                            js[str(opcionJugador1)]["Ataques"][0][str(x + 1)]["Nombre"],
                            js[str(opcionJugador1)]["Ataques"][0][str(x + 1)]["Id"],
                            js[str(opcionJugador1)]["Ataques"][0][str(x + 1)]["Tipo1"],
                            js[str(opcionJugador1)]["Ataques"][0][str(x + 1)]["Tipo2"],
                            js[str(opcionJugador1)]["Ataques"][0][str(x + 1)]["Especial"])
            listaAtaquesX.append(ataque)

        pokemonJugador1 = Pokemon(js[str(opcionJugador1)]["Nombre"], js[str(opcionJugador1)]["Vida"],
                                  js[str(opcionJugador1)]["Mana"], js[str(opcionJugador1)]["Potencia"],
                                  js[str(opcionJugador1)]["Potencia especial"], js[str(opcionJugador1)]["Defensa"],
                                  js[str(opcionJugador1)]["Defensa especial"], js[str(opcionJugador1)]["Tipo"],
                                  js[str(opcionJugador1)]["Id"], listaAtaquesX, js[str(opcionJugador1)]["Velocidad"])

        listaAtaquesY = []
        for x in range(4):
            ataque = Ataque(js[str(opcionIA)]["Ataques"][0][str(x + 1)]["Potencia"],
                            js[str(opcionIA)]["Ataques"][0][str(x + 1)]["PP"],
                            js[str(opcionIA)]["Ataques"][0][str(x + 1)]["PP"],
                            js[str(opcionIA)]["Ataques"][0][str(x + 1)]["Nombre"],
                            js[str(opcionIA)]["Ataques"][0][str(x + 1)]["Id"],
                            js[str(opcionIA)]["Ataques"][0][str(x + 1)]["Tipo1"],
                            js[str(opcionIA)]["Ataques"][0][str(x + 1)]["Tipo2"],
                            js[str(opcionIA)]["Ataques"][0][str(x + 1)]["Especial"])
            listaAtaquesY.append(ataque)

        pokemonIA = Pokemon(js[str(opcionIA)]["Nombre"], js[str(opcionIA)]["Vida"],
                                  js[str(opcionIA)]["Mana"], js[str(opcionIA)]["Potencia"],
                                  js[str(opcionIA)]["Potencia especial"], js[str(opcionIA)]["Defensa"],
                                  js[str(opcionIA)]["Defensa especial"], js[str(opcionIA)]["Tipo"],
                                  js[str(opcionIA)]["Id"], listaAtaquesY, js[str(opcionIA)]["Velocidad"])

        return pokemonJugador1, pokemonIA

    def partida(self, pokemon1, pokemon2):
        # if self.turno%2 == 0:
        eficaz = False
        print("")
        print("RONDA" + str(self.turno) + " !!")
        time.sleep(2)
        print("Es el turno de " + pokemon1.nombre)
        time.sleep(2)
        print("-Elige un movimiento-")
        for i in pokemon1.ataques:
            print(i.nombre)
        idMovimiento = input()
        print("")
        for ataque in pokemon1.ataques:
            if str(ataque.id) == idMovimiento:
                eficaz, curar, potencia, noEficaz, estad = pokemon1.atacar(pokemon2,ataque)
                return eficaz,curar, ataque, potencia, noEficaz, estad

    def partidaIA(self, pokemonIA, pokemonJugador):
        eficaz = False
        movimientos = [1,2,3,4]
        movIA = random.choice(movimientos)
        print("")
        print("RONDA" + str(self.turno) + " !!")
        time.sleep(2)
        print("Es el turno de " + pokemonIA.nombre)
        time.sleep(2)
        print(pokemonIA.nombre + " va a elegir su movimiento...")
        time.sleep(2)
        print("")
        for ataque in pokemonIA.ataques:
            if ataque.id == movIA:
                eficaz, curar, potencia, noEficaz, estad = pokemonIA.atacar(pokemonJugador, ataque)
                return eficaz,curar, ataque, potencia, noEficaz, estad

    def resumenPartida(self,pokemon1,pokemon2): #TODO: poner waits, printear el proximo ataque, si es efectivo, si ha fallado, etc
        print("")
        print(pokemon1.nombre)
        print("Vida: " + str(pokemon1.vida))
        print("Mana: " + str(pokemon1.mana))
        print("Velocidad: " + str(pokemon1.velocidad))
        print(" ")
        print(pokemon2.nombre)
        print("Vida: " + str(pokemon2.vida))
        print("Mana: " + str(pokemon2.mana))
        print("Velocidad: " + str(pokemon2.velocidad))
        print("")

    def resumenAtaque(self, pokemon1, pokemon2, ataque, eficaz, curar, potencia, noEficaz, estad):
        print("")
        time.sleep(1)
        print(pokemon1.nombre + " va a realizar " + ataque.nombre + " !")
        time.sleep(2.5)
        if ataque.tipo == "Ofensivo":
            print(pokemon1.nombre + " ha causado " + str(potencia) + " de daño a " + pokemon2.nombre)
            time.sleep(2.5)
            if eficaz == True:
                print("Es super eficaz !!")
            if noEficaz == True:
                print("Es muy poco eficaz...")
            if potencia == 0:
                print(pokemon1.nombre + " a fallado el ataque !!")
        if ataque.tipo == "Curativo":
            if curar == True:
                print(pokemon1.nombre + " se ha curado " + str(potencia) + " HP")
        if ataque.tipo == "Estadistico":
            if estad == True:
                print("Se ha reducio la defensa de " + pokemon2.nombre + " a " + str(pokemon2.defensa) + " y la defensa especial a " + str(pokemon2.defensaEspecial))
        print("")

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
    logo()
    partida.menu()
    return 0


if __name__ == '__main__':
    main()
