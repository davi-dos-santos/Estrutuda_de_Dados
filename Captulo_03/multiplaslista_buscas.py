equipamento = []
valores =[]
seriais = []
departamento = []
resposta = "S"
while resposta == "S":
    equipamento.append(input("\nEquipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamento.append(input("Departamento: "))
    resposta=input("Digite \"S\" para continuar: ").upper()

busca = input("\nDigite o nome do equipamento a buscar: ")
for indice in range(0, len(equipamento)):
    if busca == equipamento[indice]:
        print("Equipamento....:", equipamento[indice])
        print("Valor..........:", valores[indice])
        print("Serieais.......:", seriais[indice])