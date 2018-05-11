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

while num != ran:
    ran = randint(0, 5)
    if num < 0 or num > 5:
        if num < 0:
            print("O número não pode ser negativo!")
            num = int(input("Digite: \n"))  # Pedido
        elif num > 5:
            print("Tente um número menor do que 6!")
            num = int(input("Digite: \n"))  # Pedido
    else:
        if num != ran:
            print("Número digitado: {}.".format(num))
            print("VocÊ ERROU. O número correto era {}".format(ran))
            print("Tente novamente.")
            num = int(input("Digite: \n"))  # Pedido
print("Número digitado: {}.".format(num))
print("Número da máquina: {}.".format(ran))
print("Parabéns, você venceu.")
