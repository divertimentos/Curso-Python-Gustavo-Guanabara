"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
"""
aproveitamento = {
    'nome': None,
    'partidas': None,
    'gols': 0,
}

# Nome
nome = input("Qual o nome do jogador? \n" )
aproveitamento['nome'] = nome

# Partidas
partidas = int(input("Partidas jogadas: \n"))
aproveitamento['partidas'] = partidas

# Gols em cada partida
for partida in range(partidas):
    gols_partida = int(input(f"Quantos gols o {nome} fez na partida {partida+1}? \n"))
    aproveitamento['gols'] += gols_partida


print(
    f"O jogador {nome} jogou {partidas} partidas e possui um total de {aproveitamento['gols']} gols!"
)