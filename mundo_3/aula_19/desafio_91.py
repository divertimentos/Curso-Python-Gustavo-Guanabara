"""
Crie um programa onde 4 jogadores joguem um dado
e tenham resultados aleatórios.
Guarde esses resultados em um dicionário.

No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado
"""

from random import randint

players = dict()
counter = 0

print("Valores sorteados: \n")
for i in range(4):
    jogada = randint(1, 6)
    players[f"jogador {i + 1}"] = jogada

    print(f"O jogador {i + 1} tirou {jogada} pontos no dado.")

print("\nRanking dos jogadores:")
players_list = sorted(
    list(zip(players.values(), players.keys())), reverse=True)


for i, player in enumerate(players_list):
    print(
        f"{i+1}º lugar: {players_list[i][1]} com {players_list[i][0]} pontos")
    counter += 1
