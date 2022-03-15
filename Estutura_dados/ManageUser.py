from Estutura_dados.Funcoes import *
usuarios = {}

opcao = perguntar()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(usuarios)
    opcao = perguntar()

opcao = pesquisar()
while opcao == "I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao == "P":
        pesquisar(input("Qual login deseja pesquisar? "))
    opcao = pesquisar()