'''
Faça um programa que leia 5 valores números e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitados
e as suas respectivas posições na lista.
'''

lista = []
lista_menores = []
lista_maiores = [] 
maior = menor = pos_menor = pos_maior = 0

for ordinal in range(1, 6):
    lista.append(int(input(f"Digite o {ordinal}º número: \n")))


for pos, num in enumerate(lista):
    if menor == 0:  # Deszerando o contador.
        menor = num

    if num < menor:
        menor = num
    if num > maior:
        maior = num

for posi, item in enumerate(lista):
    if item == menor:
        lista_menores.append(posi)
    if item == maior:
        lista_maiores.append(posi)


print(f"Você digitou os valores: {lista}.")

print(f"O maior valor digitado foi {maior}", end="")
print(f" na(s) posição(ões) {lista_maiores}.")

print(f"O menor valor digitado foi {menor}", end="")
print(f" na(s) posição(ões) {lista_menores}.")

