'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado(inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.

Obs.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
num = int(input("Que valor você quer sacar? \n"))
cedulas = [50, 20, 10, 1]
'''

saque = int(input("Que valor você quer sacar? \n"))
notas = [50, 20, 10, 1]
cedulas = []
counter = 0

while saque > 0:
    for val in notas:
        cedulas.append(saque // val)
        saque = saque % val
#        print(f"{cedulas[counter]} notas de R${val}")
        counter += 1
counter = 0

for item in cedulas:
    if item > 0:
        print(f"{item} cédulas de R${notas[counter]}")
    counter += 1 # teste
