import json

f = open("pokemon.json", "r")
c = f.read()
f.close()
js = json.loads(c)

print("Pokemon Game inspired in Generation 1, coded by snavarrete7")
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



print(js["1"]["Ataques"][0]["1"]["Potencia"])


for x in js:
    print("--------------------------------")
    print(js[x]["Nombre"])
    print("Vida: " + str(js[x]["Vida"]))
    print("Potencia " + str(js[x]["Potencia"]))
    print("Potencia especial " + str(js[x]["Potencia especial"]))
    print("Defensa " + str(js[x]["Defensa"]))
    print("Defensa especial " + str(js[x]["Defensa especial"]))
    print("Tipo: " + str(js[x]["Tipo"]))
    print("Introduce " + x + " para seleccionar a " + js[x]["Nombre"])
    print("--------------------------------")

opcion = input("Numero del pokemon escogido: ")
print(js[opcion]["Nombre"])





