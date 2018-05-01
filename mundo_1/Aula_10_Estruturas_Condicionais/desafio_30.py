'''
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''
n = int(input("Descubra se um número é par ou ímpar: \n"))
if n % 2 == 0:
    print("O número {} é par.".format(n))
else:
    print("O número {} é ímpar.".format(n))
