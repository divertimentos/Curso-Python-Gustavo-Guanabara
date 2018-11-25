'''
Faça um programa que leia nome e peso de várias pessoas
guardando tudo em uma lista.
No final, mostre:

a: quantas pessoas foram cadastradas.
b: uma listagem com as pessoas mais pesadas
c: uma listagem com as pessoas mais leves

Obs.: Gerar uma lista com os mais leves e mais pesados
Vai depender de analisar qual é o mais leve e o mais pesado.
Se houver mais de um com esse peso, insere na lista.
O mais normal é que a lista de mais pesados tenha apenas 1 pessoa,
que é o motivo pelo qual a lista existe.

'''

lista = list()
listb = list()
counter = 0

# Atribuição dos dados nas listas:
while True:
    lista.append(str(input("Nome: \n"))) 
    lista.append(float(input("Peso (em kg): \n")))
    
    listb.append(lista[:])
    lista.clear()
    counter += 1

    pergunta = str(input("Continuar? [Sim/Não] \n")).upper()
    if pergunta[0] == "N":
        break

####

# Resposta a):
print(f"a) pessoas cadastradas: {counter}.")

####

# Breve tratamento dos dados contidos nas listas:

pesos = list()  # Lista onde estarão apenas os pesos

for i in listb:
    pesos.append(i[1])

pesos = sorted(pesos)  # Lista onde extrairei o maior e o menor valor.

menor = pesos[0]
maior = pesos[-1]

# a) pessoas mais pesadas:
mais_pesados = list()
menos_pesados = list()

####

for k in listb:  # Para cada lista dentro de listb:
    if k[1] == maior:  # Se o peso for igual a maior
        mais_pesados.append(k[0])  # Adicione seu nome à lista
    if k[1] == menor:  # Se o peso for igual a menor,
        menos_pesados.append(k[0])  # Adicione seu nome à lista

# Respostas b) e c):
print(f" b) O maior peso foi de {maior}kg. Peso de {mais_pesados}")
print(f" c) O menor peso foi de {menor}kg. Peso de {menos_pesados}.")
