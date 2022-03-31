# def hanoi(n, origem, destino, aux):
#   # Caso base: movendo um disco.
#   if n == 1:
#     print("Mova de {} para {}".format(origem, destino))
#   else:
#     # Movendo n - 1 discos de 'origem' para 'aux'.
#     hanoi(n - 1, origem, aux, destino)
#     # Movendo um único disco de 'origem' para 'destino'.
#     hanoi(1, origem, destino, aux)
#     # Movendo os n - 1 discos de 'aux' para 'destino'.
#     hanoi(n - 1, aux, destino, origem)
#
# hanoi(4, 'A', 'C', 'B')

def fatorial_recursivo(n):
  if n == 0:
    return 1
  else:
    return n * fatorial_recursivo(n - 1)

# def fatorial_iterativo(n):
#   fatorial = 1
#   for i in range(1, n + 1):
#     fatorial = fatorial * i
#   return fatorial