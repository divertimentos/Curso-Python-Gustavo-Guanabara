''' Desenvolva um programa que leia o primeiro termo e a razão
de uma PA (Progressão Aritmética).
No final, mostre os 10 primeiros termos dessa progressão.'''

prim = int(input("Primeiro termo: \n"))
raz = int(input("Digite a razão da PA: \n"))
# pa = prim + raz
pa = prim
counter = 0
# Este é o jeito burro de fazer:

# for i in range(prim, prim + 20, raz):
#    print(i)

# Este é um jeito quase ideal de fazer:
for i in range(prim, prim + 10):
    pa += raz
    counter += 1
    print("Termo {}: {}.".format(counter, pa))

# Ainda preciso dar um jeito elegante de consertar o primeiro termo
