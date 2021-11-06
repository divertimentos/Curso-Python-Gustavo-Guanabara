"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros:
o nome de um jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""


def ficha(nome_jogador, numero_gols):
    return f"O jogador {nome_jogador.upper()} fez {numero_gols} gols."


nome = str(input("Nome do jogador: \n"))
if len(nome) == 0:
    nome = "<desconhecido>"

gols = str(input("Número de gols: \n"))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0


print(ficha(nome, gols))
