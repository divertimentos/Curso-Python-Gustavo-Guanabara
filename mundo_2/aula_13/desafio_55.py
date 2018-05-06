''' Faça um programa que leia o peso de cinco pessoas
No final, mostre qual foi o maior e o menor peso lidos'''
maior = 0
for i in range(5):
    peso = float(input("Digite um peso: \n"))
    if peso > maior:
        maior = peso

print("O maior peso é {}kg".format(maior))
