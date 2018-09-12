''' Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou, 
no final do jogo.'''

from random import randint
from time import sleep

victories = 0

while True:
    player = int(input("Escolha um número: \n"))
    #  Controle de exceções:
    if player < 0:
        print("Digite um inteiro positivo menor do que dez.")
    elif player > 10:
        print("Digite um inteiro menor do que 10")
    else:  # Se entre 0 e 10, então rode:
        computer = randint(0, 10)  # Jogada da máquina
        choice = str(input("Ímpar ou par? [I / P] \n")).strip().upper()
        if choice == "P":  # Se você escolheu par:
            print("Você escolheu: PAR!")
            soma = player + computer
            if soma % 2 == 0:  # Se deu par:
                victories += 1
                sleep(1)
                print(f"O computador escolheu {computer}.")
                print(f"{soma} é par, então você ganhou!")
            else:  # Se deu ímpar:
                sleep(1)
                print(f"O computador escolheu {computer}.")
                print(f"{soma} é ímpar, então você perdeu.")
                print(f"Vitórias consecutivas: {victories}")
                break
        
        elif choice == "I":  # Se você escolheu ímpar:
            soma = player + computer
            print("Você escolheu ÍMPAR!")
            if soma % 2 != 0:  # Se a soma deu ímpar:
                victories += 1
                sleep(1)
                print(f"O computador escolheu {computer}.")
                print(f"{soma} é ímpar, então você ganhou!")
            else:  # Se deu par:
                sleep(1)
                print(f"O computador escolheu {computer}.")
                print(f"{soma} é par, então você perdeu!")
                print(f"Vitórias consecutivas: {victories}")
                break
        else:
            print("Escolha Ímpar ou Par!")
            sleep(1.5)
            print("Seu bosta!")
            sleep(1)
