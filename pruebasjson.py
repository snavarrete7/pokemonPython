import json

f = open("pokemon.json", "r")
c = f.read()
f.close()
js = json.loads(c)

m = input()

print(js[m]["Ataques"][0]["Ataque1"]["Potencia"])