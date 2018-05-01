# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
# Método que eu usei antes de assistir às aulas do Guanabara:
'''
# Primeira parte: Estabelecimento de variáveis e contadores
nomes = ["Black Panther", "Solid Snake", "Kendrick Lamar", "Shadow the Hedgehog"]
nomes = sample(nomes, len(nomes))  # Gerando aleatoriedade na lista de alunos
chosen = []  # Lista que será preenchida com os nomes dos alunos
counter = 3  # Contador que será usado para parar o while
numeracao = 0  # Contador que será usado para enumerar os alunos no print final

# Segunda parte: loop e inserção de itens na lista chosen
while len(nomes) > 0:  # Enquanto o contador não estiver vazio
    chosen.append(nomes[-1])  # Adicione à lista chosen o último item, gerado aleatoriamente, da lista nomes
    nomes.pop()  # Remova o último item da lista nomes
    counter -= 1  # Incremente a condição de parada do while em -1

# Terceira parte: print da lista final pronta
print("A lista de apresentação de trabalhos dos alunos, gerada aleatoriamente, é esta: \n")
for nome in chosen:  # Para cada item da lista chosen, recém-completa
    numeracao += 1  # Incremente em 1 o contador numeracao
    print("%0.f: %s" % (numeracao, nome))  # E printe a mensagem final
'''
# Método do Guanabara:

nomes = ["Black Panther", "Solid Snake", "Kendrick Lamar", "Shadow the Hedgehog"]
shuffle(nomes)
print("A lista de apresentação é {}.".format(nomes))
