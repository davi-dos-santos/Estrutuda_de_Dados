usuarios = {}
email = ["xptoO@xpto.com", "xppp@xppp.com"]

tupla = list(enumerate(email))

print(tupla)

for chave in range(0, len(tupla)):
    print("email: ", tupla[chave] [1])
    usuarios[tupla[chave]] = [input("Nome: "), input("Nivel: ")]

print("-----------------------------------------")
for chave, dado in usuarios.items():
    print("Usuaior: ", chave[0])
    print("email: ", chave[1])
    print("Nome: ", dado[0])
    print("Nivel: ", dado[0])