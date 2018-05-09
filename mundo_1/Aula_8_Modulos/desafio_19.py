# Deixando em standby este código que eu achei lindo, mas que infelizmente meus conhecimentos atuais sobre dicionários não permitiram que eu o concluísse.

# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o do escolhido.
import random

nomes = ["Black Panther", "Solid Snake", "Kendrick Lamar", "Shadow the Hedgehog"]
classe = {}
contador = 1

num = random.randint(1, 4)

for nome in nomes:  # Para cada nome na lista nomes
    classe[nome] = contador  # Adicione a esse nome o valor atual da variável contador
    contador += 1  # Atualize o contador para que ele chegue a 4 no fim dos loops
    # if num == classe[value]:
for valor in classe.values():
    if num == valor:
        print("teste dict: ", classe.get("Black Panther"))

print(classe.values())

# for i in range(1, num + 1):
#    escolhido = num
