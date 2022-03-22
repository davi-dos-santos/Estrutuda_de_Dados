basedados = []
with open("iris.data", "r") as arquivo:
    for registro in arquivo.readlines():
        basedados.append(registro.split(","))

print(basedados, "\n")

print(float(basedados[0][0]), "e", float(basedados[0][1]))