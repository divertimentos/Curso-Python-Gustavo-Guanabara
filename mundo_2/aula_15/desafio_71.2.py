'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado(inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.

Obs.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

num = int(input("Que valor você quer sacar? \n"))

cedulas = [50, 20, 10, 1]

while num > 0:
    for i in cedulas:
        cedulas = num // i
        num = num % i
        if cedulas > 0:
            print(f"{cedulas} notas de R${i}")