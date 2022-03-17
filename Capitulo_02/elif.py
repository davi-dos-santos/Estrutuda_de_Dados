nome = input("Digite o nome: ")
idade = int(input("Digite sua idade: "))
doenca = input("Suspeita de doença (sim/não): ").upper()
if idade >= 65:
    print("O paceinte " + nome + " Possui atemdiento prioritario")
elif doenca == "SIM":
    print("O paceinte " + nome + " sala de espera")
else:
    print("O paceinte " + nome + " Não possui atemdiento prioritario")
print("Fim!")