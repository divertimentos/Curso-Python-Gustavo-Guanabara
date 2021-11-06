# help(print)
# print(input.__doc__)

# def contador(i, f, p):
#     """
#     Faz uma contagem e mostra na tela.
#     :param i: início da contagem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return sem retorno
#     """
#     c = i
#     while c <= f:
#         print(f"{c}", end=", ")
#         c+= p
#     print("FIM!")

# contador(2, 10, 2)

# print(help(contador))

# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     print(f"A soma vale: {s}.")
# somar(3, 2, 5)
# somar(8, 4)
# somar()

# def funcao():
#     variavel = "dentro"
#     print(f"Variável dentro recebe: {variavel}")

# variavel = "fora"
# funcao()
# print(f"Variável fora recebe: {variavel}")

# def funcao(parametro):
#     global a
#     a = 8
#     print(f"'a' vale {a}")
# a = 5
# funcao(a)
# print(f"'a' fora vale {a}")

### RETORNO

# def somar(a=3, b=0, c=0):
#     s = a + b + c
#     return s

# print(somar(3, 2, 5))
# print(somar(2, 2))
# print(somar(6))

# r1 = somar(3, 2, 5)
# r2 = somar(2, 2)
# r3 = somar(6)

# print(f"Os resultados foram {r1}, {r2} e {r3}.")

### PARTE PRATICA DA AULA:


def fatorial(num=1):
    fatorial = 1
    for i in range(num, 0, -1):
        fatorial *= i
    return fatorial


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

# print(f"Os resultados são: {f1}, {f2} e {f3}")

# def par(n=0):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
# num = int(input("Digite um número: \n"))
# if par(num):
#     print(f"É par!")
# else:
#     print(f"É ímpar!")
