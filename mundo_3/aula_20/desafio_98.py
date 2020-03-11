from time import sleep

"""
Faça um programa que tenha uma função chamada contador(), que recebe três parâmetros:
início, fim e passo
E realize a contagem

Seu programa tem que realizar três contagens através da função criada

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) Uma contagem personalizada

--> print(f"{valor} ", end="")  # Exemplo de print espaçado
"""

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}.")

    if inicio < fim:
        counter = inicio
        while counter <= fim:
            print(f"{counter} ", end="")
            sleep(0.2)
            counter += passo
        print("Fim")
    else:
        counter = inicio
        while counter >= fim:
            print(f"{counter} ", end="")
            sleep(0.2)
            counter -= passo
        print("Fim!")

inicio = int(input("Início: \n"))
fim = int(input("Fim: \n"))
passo = int(input("Passo: \n"))

contador(1, 10, 1)
contador(10, 0, 2)
contador(inicio, fim, passo)