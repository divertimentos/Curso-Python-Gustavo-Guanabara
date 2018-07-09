'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os valores ímpares digitados, respectivamente.

Ao final, mostre o conteúdo das três listas geradas.
'''
lista = []
pares = []
impares = []

while True:
    lista.append(int(input("Digite um número: \n")))
    cont = str(input("Quer continuar? \n")).strip().upper()
    if cont[0] == "S":
        print("Continuando.")
    elif cont[0] == "N":
        print("Programa finalizado.")
        break
    else:
        print("Digite uma resposta válida.")


for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f"Lista de números digitados: {lista}.")
print(f"Lista de números pares: {pares}.")
print(f"Lista de números ímpares: {impares}.")
