'''
Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares
Se o valor digitado for ímpar, desconsidere-o.'''

s = 0
for i in range(0, 6):
    num = int(input("Digite um número: \n"))
    if num % 2 == 0:
        s += num
print("Somas: {}.".format(s))
