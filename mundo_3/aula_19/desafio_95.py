"""
Aprimore o DESAFIO 093 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes de aproveitamento 
de cada jogador.
"""


aproveitamento = dict()
gols = 0
soma_gols = 0
lista_gols = list()
infos_jogadores = list()

while True:
    # Nome
    aproveitamento['nome'] = input("Qual o nome do(a) jogador(a)? \n")
    nome_jogador = aproveitamento['nome']

    # Partidas
    aproveitamento['partidas'] = int(input("Partidas jogadas: \n"))
    partidas_jogadas = aproveitamento['partidas']
    
    # Gols
    for partida in range(partidas_jogadas):
        gols_partida = int(input(f"Quantos gols {nome_jogador} fez na partida {partida+1}? \n"))
        lista_gols.append(gols_partida)
        aproveitamento['lista_gols'] = lista_gols.copy()

    # Soma gols
    aproveitamento['soma_gols'] = sum(lista_gols)
    
    # Inserção na listona
    infos_jogadores.append(aproveitamento.copy())
    lista_gols.clear()

    # Continue?
    continuar = input("Quer continuar? [S/N] \n")
    continuar = continuar.upper()
    if continuar[0] == "N":
        break

print(f"{'cod':^5} {'nome':^10} {'gols':<25} {'total':<25}")
for cod, jogador in enumerate(infos_jogadores):
    print(f"{cod:^5} {jogador['nome']:^10} {jogador['lista_gols']!s:<25s} {jogador['soma_gols']:<25}")
