def perguntar():
    return input("O que deseja realziar?\n" +
              "<I> Iserir usuairo\n" +
              "<P> Pesuuisar usuario\n" +
              "<E> Excluir usuairo\n" +
              "<L> Listar usuarios: ").upper()

def inserir(dicionario):
    dicionario[input("Chave: ").upper()] = [input("Nome: ").upper(),
                                            input("Data: "),
                                            input("estação: ").upper()]
    salvar(dicionario)

def salvar(dicionario):
    with open("BD.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))