'''
Faça um programa que leia o sexo de uma pessoa
mas só aceite os valores "M" ou "F".
Caso esteja errado, peça a digitação novamente
até ter um valor correto.
'''

sex = str(input("Digite M ou F: \n")).strip().upper()[0]
while sex not in "MmFf":
    sex = str(input("Ô SEU CARALHO, digita só M ou F: \n")).strip().upper()[0]
print("Sexo {} registrado com sucesso.".format(sex))
