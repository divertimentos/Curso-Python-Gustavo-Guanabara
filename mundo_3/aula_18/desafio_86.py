'''
Crie um programa que crie uma matriz 3.3
e preencha com valores lidos pelo teclado.

No final, mostre a matriz na tela com a formatação correta
'''

lista = list()
listb = list()

for i in range(0, 3):
    for j in range(0, 3):
        listb.append(int(input(f"Digite um valor para [{i}, {j}]: \n")))
    
    lista.append(listb[:])
    listb.clear()

for l in lista:
    print(l)
