"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros:
o nome de um jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""

def ficha(nome_jogador, numero_gols):
    if len(nome_jogador) == 0:
        nome_jogador = "<desconhecido>"
    if len(numero_gols) == 0:
        numero_gols = 0

    return f"O jogador {nome_jogador.upper()} fez {numero_gols} gols."
nome = str(input("Nome do jogador: \n"))
gols = (input("Número de gols: \n"))

print(ficha(nome, gols))