'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.

'''
from random import randint
from time import sleep
ran = randint(0, 5)

print("--=--" * 15)
print("Vou pensar em um número entre 0 e 5 e você deverá tentar adivinhá-lo.")
print("--=--" * 15)
num = int(input("Em qual número você acha que eu pensei?: \n"))
print("Pensando...")
sleep(1)

if num > 5 or num < 0:
    if num < 0:
        print("O número não pode ser negativo.")
    else:
        print("Dica: o número está entre 0 e 5!")
else:
    if num == ran:
        print("Número digitado: {}.".format(num))
        print("Parabéns, você venceu!")
    else:
        print("Número digitado: {}.".format(num))
        print("VOCÊ ERROU. \nO número correto era {}. Tente novamente.".format(ran))
