# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

# ex.: digite um número: 1834
# unidade: 4
# dezenas: 3
# centenas: 8
# milhares: 1

num = int(input("Digite um número a ser fatiado: \n"))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))
