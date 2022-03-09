def perguntar():
    resposta = input("O que deseja realziar? \n"+
               "(I) Inserir um usuario \n" +
               "(P) Pesquisar um usuario \n" +
               "(E) Excluir um usaurio \n" +
               "(L) Listar um usario").upper()
    return resposta

def inserir(dicinonario):
    dicinonario[input("Digite o Login: ").upper() ] = [input("digite o nome: ").upper(),
                                                       input("difite a ultima data de acesso"),
                                                       input("difite a ultima estaçao acessada: ").upper()]