def perguntar():
    return input("O que deseja realziar?\n" +
              "<I> Iserir usuairo\n" +
              "<P> Pesuuisar usuario\n" +
              "<E> Excluir usuairo\n" +
              "<L> Listar usuarios: ").upper()

def inserir(dicionaio):
    dicionaio[input("Chave: ").upper()] = [
        input("Nome: ").upper(),
        input("Data: "),
        input("estação: ").upper()]
