''' Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
2 para hexadecimal
'''
num = float(input("Digite um número a ser convertido: \n"))
base = int(input('''Escolha a base da conversão:
Para binário digite: 1
Para octal digite: 2
Para hexadecimal digite: 3

Sua escolha: \n'''))

if base == 1:
    print("Você escolheu binário.")
elif base == 2:
    print("Você escolheu octal.")
elif base == 3:
    print("Você escolheu hexadecimal.")
else:
    print("Por favor, escolha apenas uma das 3 opções.")
