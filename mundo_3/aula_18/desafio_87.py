'''
Aprimore o desafio anterior, mostrando no final:

a: a soma de todos os valores pares digitados
b: a soma dos valores da terceira coluna
c: o maior valor da segunda linha
'''

lista = list()
listb = list()


for i in range(0, 3):  # Para cada linha
    for j in range(0, 3):  # Para cada coluna em cada linha
        listb.append(int(input(f"Digite um valor para [{i}, {j}]: \n")))

    lista.append(listb[:])  # Copie a linha para listb
    listb.clear()

for l in lista:
    print(l)

# Resposta A: soma de todos os valores pares digitados
soma = 0

for i in range(3):
    for j in range(3):
        if lista[i][j] % 2 == 0:
            soma += lista[i][j]

print(f"Soma dos valores pares: {soma}.")

# Reposta B: soma dos valores da terceira coluna:
soma_coluna = 0

for i in range(3):
    for j in range(3):
        if j == 2:  # colune 3
            soma_coluna += lista[i][j]
print(f"Soma terceira coluna: {soma_coluna}.")

# Resposta C: o maior valor da segunda linha:


maior = 0

for i in range(3):
    for j in range(3):
        if i == 1:  # linha 2
            if lista[i][j] > maior:
                maior = lista[i][j]
print(f"Maior valor da segunda linha: {maior}.")
