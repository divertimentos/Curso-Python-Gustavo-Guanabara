# Desafio 17: Faça um programa que leia o comprimento do cateto oposto (co) e do cateto adjacente (ca) de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

co = float(input("Cateto oposto: \n"))
# co = math.pow(co, 2)  # co = 9
ca = float(input("Cateto adjacente: \n"))
# ca = math.pow(ca, 2)  # ca = 16

hi = hypot(co, ca)

# print("A hipotenusa dos números %.1f e %.1f é: %.1f!" % (co, ca, hipotenusa))
print("A hi dos números {} e {} é {:.2f}.".format(co, ca, hi))
