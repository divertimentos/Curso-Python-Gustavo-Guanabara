'''
Crie uma tupla preenchida com os 20 primeiros colocados
da Tabela do Campeonato Brasileiro,
na ordem de colocação.
Depois mostre:
a) apenas os 5 primeiros colocados
b) os últimos 4 colocados da tabela
c) uma lista com os times em ordem alfabética
d) em que posição na tabela está o time da Chapecoense
'''

times = (
    "Atlético", "Flamengo", "Corinthians", "Palmeiras", "Fluminense",
    "América-MG", "São Paulo", "Grêmio", "Vasco da Gama", "Botafogo",
    "Sport Recife", "Cruzeiro", "EC Vitória", "Santos", "Chapecoense",
    "Atlético-PR", "Internacional", "Bahia", "Ceará SC", "Paraná"
)
# a) os primeiros 5 colocados:
print(f"a) Primeiros 5 colocados do Brasileirão: \n{times[0:6]}")

# b) os últimos 4 colocados:
print(f"b) Últimos 4 colocados: \n{times[-4:]}")

# c) Times em ordem alfabética:
print(f"\nTimes em ordem alfabética: \n")
for time in sorted(times):
    print(time)


# d) em que posição da tabela está o time da Chapecoense:
chape = times.index("Chapecoense") + 1
print(f"A Chapecoense está na {chape}ª posição.")
