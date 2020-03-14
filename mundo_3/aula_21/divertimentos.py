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

def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f"A soma vale: {s}.")
# somar(3, 2, 5)
somar(8, 4)
somar()