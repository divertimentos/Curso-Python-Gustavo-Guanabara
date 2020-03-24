"""
Crie um programa que tenha a função leia_int(), 
que vai funcionar de forma semelhante à função input do Python,
só que fazendo a validação para aceitar apenas um valor numérico.

ex.:
n = leia_int("Digite um n")
"""

def leia_int(entrada_usuario):
    while True:
        numero = input(f"{entrada_usuario} \n")
        if numero.isnumeric():
            return numero
            break
        else:
            print("\033[93m ERRO! Digite um número inteiro válido!")

n = leia_int("Digite um número:")
print(f"Você acabou de digitar o número: {n}.")