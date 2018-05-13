''' Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer
'''

from random import randint
from time import sleep

ran = -1
counter = 0

num = int(input("Em qual número você acha que eu pensei? \n"))  # Pedido

ran = randint(0, 5)
while num != ran:
    if num < 0 or num > 5:  # entrada errada do usuário
        if num < 0:
            print("O número não pode ser negativo!")
            num = int(input("Digite: \n"))  # Pedido
        elif num > 5:
            print("Tente um número menor do que 6!")
            num = int(input("Digite: \n"))  # Pedido
    else:
        if num != ran:
            if ran > num:
                print("Você errou! \nDica: digite um número maior.")
                print("Número digitado: {}.".format(num))
                num = int(input("Tente novamente: \n"))  # Pedido
            if ran < num:
                print("Você errou! \nDica: digite um número menor.")
                print("Número digitado: {}.".format(num))
                num = int(input("Tente novamente: \n"))  # Pedido
    counter += 1
print("Número digitado: {}.".format(num))
print("Número da máquina: {}.".format(ran))
print("Parabéns, você venceu.")
print("Número de tentativas: {}.".format(counter))
