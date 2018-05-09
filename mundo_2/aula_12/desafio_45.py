from random import choice
from time import sleep
'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''
lista = ["pedra", "papel", "tesoura"]
print('''
COMPUTADOR: Vamos jogar Pedra, Papel, Tesoura!
As regras são as seguintes:
- Papel vence Pedra e perde para Tesoura
- Pedra vence Tesoura e perde para Papel
- Tesoura vence Papel e perde para Pedra
''')

jogador = str(input("Você escolhe pedra, papel ou tesoura? \n")).lower()

print("JO")
sleep(0.50)
print("KEN")
sleep(0.5)
print("PÔ!!!")

computador = choice(lista)
vencedor = ""
print('''
Jogador: {}
Computador: {}'''.format(jogador, computador))

if (jogador != "pedra" and jogador != str("papel") and jogador != str("tesoura")):
    print("{} não é uma opção válida. Escolha pedra, papel ou tesoura.".format(jogador))
elif jogador == computador:
    print("Empate. Vamos jogar novamente.")

# Jogadas válidas:

elif jogador == "pedra" and computador == "tesoura":  # Pedra x Tesoura: Pedra
    print("Pedra vence tesoura. Jogador ganhou.")
elif jogador == "tesoura" and computador == "pedra":  # Tesoura x Pedra: Pedra
    print("Pedra vence tesoura. Computador ganhou.")

elif jogador == "pedra" and computador == "papel":  # Pedra x Papel: Papel
    print("Papel vence pedra. Computador ganhou.")
elif jogador == "papel" and computador == "pedra":  # Papel x Pedra: Papel
    print("Papel vence pedra. Jogador ganhou.")

elif jogador == "tesoura" and computador == "papel":  # Tesoura x Papel: Tesoura
    print("Papel vence tesoura. Computador ganhou.")
elif jogador == "papel" and computador == "tesoura":  # Papel x Tesoura: Tesoura
    print("Papel vence tesoura. Jogador ganhou.")
