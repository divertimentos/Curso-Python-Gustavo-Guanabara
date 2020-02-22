"""
Aprimore o DESAFIO 093 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes de aproveitamento 
de cada jogador.
"""


aproveitamento = dict()
gols = 0
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
    if partidas_jogadas > 0:
        for partida in range(partidas_jogadas):
            gols_partida = int(input(f"Quantos gols {nome_jogador} fez na partida {partida+1}? \n"))
            lista_gols.append(gols_partida)
    aproveitamento['lista_gols'] = lista_gols
    # lista_gols = aproveitamento['lista_gols']


    # Inserção na listona
    infos_jogadores.append(aproveitamento.copy())

    # Continue?
    continuar = input("Quer continuar? [S/N] \n")
    continuar = continuar.upper()
    if continuar == "N":
        break

print("Infos")
print(infos_jogadores)

print(f"{'cod':^5} {'nome':^5} {'gols':^5} {'total':<25}")
for cod, jogador in enumerate(infos_jogadores):
    print(f"{cod:^5} {jogador['nome']:^5} {jogador['lista_gols']} {sum(jogador['lista_gols']):<10}")