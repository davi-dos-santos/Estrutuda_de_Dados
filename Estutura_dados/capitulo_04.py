from Estutura_dados.Funcoes import *
usuarios = {}
opcao = perguntar()
while opcao =="I" or opcao=="P" or opcao=="E" or opcao=="L":
 if opcao=="I":
  inserir(usuarios)
 opcao = perguntar()


#usuarios={}
#opcao=input(" O que deseja fazer \n"+
 #           "(I) Inserir um usuario \n"+
  #          "(P) Pesquisar um usuario \n"+
   #         "(E) Excluir um usaurio \n"+
    #        "(L) Listar um usario \n").upper()
#while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
 #if opcao == "I":
  #chave = input("Digite o login: \n").upper()
  #nome = input("Digite o Nome: \n").upper()
  #data = input("Digite a última data de acesso: \n").upper()
  #estacao = input("Quado a ultima estaçai acesada: \n").upper()
  #usuarios[chave] = [nome, data, estacao]
 #opcao = input("O que deseja realziar? \n"+
  #             "(I) Inserir um usuario \n" +
  #             "(P) Pesquisar um usuario \n" +
  #             "(E) Excluir um usaurio \n" +
  #             "(L) Listar um usario").upper()