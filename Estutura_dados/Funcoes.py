def perguntar():
    resposta = input("O que deseja realziar? \n"+
               "(I) Inserir um usuario \n" +
               "(P) Pesquisar um usuario \n" +
               "(E) Excluir um usaurio \n" +
               "(L) Listar um usario \n").upper()
    return resposta

def inserir(dicinonario):
    dicinonario[input("digite Login: ").upper()]=[
            input("Digete nome: "),
            input("data ultimo acesso: "),
            input("ultima estação: ").upper()]

def pesquisar(dicinonario, chave):
    lista = dicinonario.get (chave)
    if lista!=None:
        print("Nome............: \n"+ lista[0])
        print("Ultimo accesso..: \n" + lista[1])
        print("Ultima estaçaõ..: \n" + lista[2])

def excluir(dicinonario, chave):
    if dicinonario.get(chave) != None:
        del dicinonario[chave]
    print("Objeto eliminado")

def listar(dicinonario):
    for chave, valor in dicinonario.intms():
        print("Obejto.....")
        print("Login: ", chave )
        print("dados: ", valor)
