from Captulo_05.funcoes import *

usuarisos = {}
opcao = perguntar()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(usuarisos)
    opcao = perguntar()