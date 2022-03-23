# # def nome da funcao (parametro1, parametros2, ...)
# # corpo da funcao
#
# def foo (n):
#     return n
#
# print(foo(10))

# def foo (n):
#     print("o valor do paraametro é: ", n)
#
# def elevado_ao_quadrado(n):
#     return n ** 2
# #
# print(elevado_ao_quadrado(5))
#
# def foo (n):
#     print("o valor do paraametro é: ", n)
#
# def elevado_ao_quadrado(n):
#     return n ** 2
#
# def potencia(n, pot):
#     return n ** pot
#
# print(potencia(2, 10))

# def foo (n):
#     print("o valor do paraametro é: ", n)
#
# def elevado_ao_quadrado(n):
#     return n ** 2
#
# def potencia(n, pot):
#     return n ** pot
#
# def eh_positivo(n):
#     return n >= 0
#
# print(eh_positivo(10))

# Exemplo de função que retorna mais de um valor.
# def quociente_resto(x, y):
#     quociente = x // y
#     resto = x % y
#     return (quociente, resto)
#
# print("Quociente e resto: ", quociente_resto(9, 4))

# # funções anônimas
def eleva_ao_quadrado(n):
    return n ** 2

# Função map sem o uso de função lambda.
print(list(map(eleva_ao_quadrado, range(6))))

# # Função map com função lambda.
# print(list(map(lambda x: x ** 2, range(5))))

# # Exemplo mais elaborado de função em Python.
# def fatorial(n):
#     fat = 1
#     while n > 1:
#         fat *= n
#         n -= 1
#     return fat
#
# print("O fatorial de {} é {}".format(6, fatorial(6)))

