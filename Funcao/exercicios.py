################################ exercicios #########################
# # minha resposta  1
# def numero(n):
#     return n + 1
#
# print(numero(0), "\n", numero(1), numero(1), "\n", numero(2), numero(2), numero(2), "\n....." )

# #Resolução  1
# def numero(n):
#     for i in range(n):
#         i += 1
#         print(str(i) * i)
#
# n = int(input('Digite um número: '))
# numero(n)

#--------------------------------------------------------

# # minha resposta 2
# def numero(n):
#     for i in range(n):
#         i += 1
#         print(str(i) * (i))
#
# n = int(3)
# numero( n )

#Resolução  2
# def numero(n):
#     for i in range(1, n + 1):
#         for a in range(1, i + 1):
#            print(a, end= " ")
#         print(" ")
#
# n = int(3)
# numero( n )

#--------------------------------------------------------

# # minha resposta 3
# def argumento(n):
#     return n + 1
#
# n = input("digite 3 numeros: ")
# print(list(map(argumento(5, 3, 5), range(3))))
# #print("A soma dos 3 numemeros é: ", (n + n + n))

# #Resolução  3
# def argumento(a, b, c):
#     return a + b + c
#
# print(argumento(3, 5 ,5))

#--------------------------------------------------------

# # minha resposta 4
