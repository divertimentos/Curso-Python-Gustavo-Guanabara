# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o do escolhido.

from random import choice
'''
nomes = ["Black Panther", "Solid Snake", "Kendrick Lamar", "Shadow the Hedgehog"]
counter = 0
num = random.randint(0, 3)

for nome in range(len(nomes)):
    if num == nome:
        print("O aluno escolhido é {}, cujo número é {}.".format(nomes[nome], counter))
    counter += 1
'''
nomes = ["Black Panther", "Solid Snake", "Kendrick Lamar", "Shadow the Hedgehog"]

escolhido = choice(nomes)
print("O aluno escolhido é {}.".format(escolhido))
