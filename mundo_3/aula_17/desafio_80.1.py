'''
Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção
(sem usar o sort()).

No final, mostre a lista ordenada na tela.
'''

lista = []

for i in range(0, 5):
    num = int(input(f"Digite um número ({i + 1}/5): \n"))
    if len(lista) == 0:  # Deszerando
        lista.append(num)
    else:
        if num > lista[-1]:  # Maior que o último
            lista.append(num)
        elif num < lista[0]:  # Menor que o primeiro
            lista.insert(0, num)
        else:
            if num < lista[1]:
                lista.insert(lista[1], num)
            # elif num        

    print(f"Índice atual: {i}")
    print(f"Índice lista atual: {lista[i]}.")



    print(f"Lista parcial: {lista}.")
