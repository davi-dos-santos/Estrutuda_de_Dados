# # w = criar aquivo, podendo tambem reescrever em cima do já criado
# with open("primeiro_arquivo.txt", "w") as arquivo:
#     arquivo.write("\n primeira linha do arquivo py")
#
# # a = edita arquivo, aplicando escrita em linhas
# with open("primeiro_arquivo.txt", "a") as arquivo:
#     arquivo.write("\n segunda linha do arquivo py")
#
# # r = leitura do arquivo, imprime as informações salvas
# with open("primeiro_arquivo.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

with open("primeiro_arquivo.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)