'''
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando
a estrutura while
'''

prim = int(input("Primeiro termo: \n"))
raz = int(input("Razão da PA: \n"))

dec = (prim + (10 - 1) * raz)  # Fórmula do enésimo termo (PA).

counter = prim
while counter <= dec:
    print("{}".format(counter))
    counter += raz
