'''
Crie um programa que vai ler vários números e colocá-los em uma lista
Depois disso, mostre:
a) quantos números foram digitados.
b) a lista de valores, ordenada de forma decrescente
c) se o valor 5 foi digitado e está ou não na lista.
'''

lista = []

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

print(f"{len(lista)} números foram digitados.")

lista.sort(reverse=True)
print(f"Esta é a lista ordenada decrescentemente {lista}")

if 5 in lista:
    print(f"O valor 5 foi digitado.")
else:
    print("O valor 5 não foi digitado.")
