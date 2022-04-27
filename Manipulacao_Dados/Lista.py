parentese = str(input("Digite os parênteses para validar:"))
lista = []
for x in parentese:
    if parentese == "(":
        lista.append("(")
    if parentese == ")":
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(")")
            break

if len(lista) == 0:
    print("OK")

else:
    print("Erro")
