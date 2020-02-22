"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
"""

aproveitamento = dict()
gols_total = 0

# Nome
aproveitamento['nome'] = input("Qual o nome do(a) jogador(a)? \n" )

# Partidas
aproveitamento['partidas'] = int(input("Partidas jogadas: \n"))

# Gols em cada partida
for partida in range(aproveitamento['partidas']):
    gols_partida = int(input(f"Quantos gols o jogador {aproveitamento['nome']} fez na partida {partida +1}? \n"))
    gols_total += gols_partida
aproveitamento['gols_total'] = gols_total


print(
    f"O jogador {aproveitamento['nome']} jogou {aproveitamento['partidas']} partidas e fez um total de {aproveitamento['gols_total']} gols."
)