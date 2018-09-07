'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.

O programa vai perguntar quantos jogos serão gerados 
e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
'''
from random import randint
from time import sleep

palpites = list()

n = int(input("Quantos jogos? :\n"))

'''
for i in range(n):
    for j in range(6):
        sleep(1)
        print(f"teste{j}.")
        palpites.append(randint(1, 60))
    sleep(1)
    print(f"Jogo {i+1}: {palpites}")
    palpites.clear()
'''
'''
for jogo in range(n):
    while len(palpites) < 6:
        for num in palpites:
            if randint(1, 60) != num:
                palpites.append(randint(1, 60))
    sleep(1)
    print(f"Jogo: {palpites}.")
'''

