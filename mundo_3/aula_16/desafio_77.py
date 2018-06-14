'''
Crie um programa que tenha uma tupla com várias palavras
(não usar acentos).
Depois disso, você deve mostrar, para cada palavra,
quais são as suas vogais
'''

tupla = (
    "Galadriel", "Luthien Tinuviel", "Erik Killmonger", 
    "Kendrick Lamar", "Charlotte Galves", "Roberta Pires", "Amanda"
    )

vogais = ["a", "e", "i", "o", "u"]

for nome in tupla:
    nome = str(nome).lower()
    lista = []

    for letra in nome:
        for i in vogais:
            if letra == i:
                lista.append(letra)

    print(f"{nome.capitalize()}: {lista} - {len(lista)} vogais")
    del(lista)
