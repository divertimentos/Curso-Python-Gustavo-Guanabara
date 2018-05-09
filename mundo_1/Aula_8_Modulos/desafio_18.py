# Desafio 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians

ang = float(input("Digite um ângulo de uma circunferência (ou seja, entre 0º e 360º): \n"))

seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))

print("O ângulo de {} tem o seno de {:.2f}.".format(ang, seno))
print("O ângulo de {} tem o cosseno de {:.2f}.".format(ang, coss))
print("O ângulo de {} tem a tangente de {:.2f}.".format(ang, tang))
