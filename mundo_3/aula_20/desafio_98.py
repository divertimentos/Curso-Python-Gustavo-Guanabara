"""
Faça um programa que tenha uma função chamada contador(), que recebe três parâmetros:
início, fim e passo
E realize a contagem

Seu programa tem que realizar três contagens através da função criada

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) Uma contagem personalizada
"""

# exemplo de print que o desafio quer:
def contador(*num):
    for valor in num:
        print(f"{valor} ", end="")
    print("Fim!")

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 5, 2)