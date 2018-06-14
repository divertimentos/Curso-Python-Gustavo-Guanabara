'''
Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extenso de zero até vinte

Seu programa deverá ler um número pelo teclado
(entre 0 e 20)
e mostrá-lo por extenso'''

extensos = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito",
    "nove", "dez", "onze", "doze", "treze", "catorze", "quinze",
    "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
    )
while True:
    n = int(input("Digite um número de 0 a 20: \n"))
    if n >= 0 and n <= 20:
        print(f"Você digitou: {extensos[n]}.")
        break
    else:
        print("Tente novamente.", end=" ")
