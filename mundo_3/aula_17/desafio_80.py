'''
Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção
(sem usar o sort()).

No final, mostre a lista ordenada na tela.
'''

lista = []

for i in range(1, 6):
    num = int(input(f"Digite um número ({i}/5): \n"))

    if len(lista) == 0:  # Tirando do zero.
        lista.append(num)
        print(f"Número {num} adicionado na posição {lista.index(num)} da lista.")

    else:
        if num < lista[0]:  # Número no início absoluto da lista.
            lista.insert(0, num)
            print(f"Número {num} adicionado no início da lista.")

        elif num > lista[-1]:  # Número no final absoluto da lista.
            lista.append(num)
            print(f"Adicionado na posição no final da lista.")

        else:
            for j in lista:
                if num > j:
                    lista.insert(j, num)
        print(f"Lista ordenada parcial: {lista}.")

