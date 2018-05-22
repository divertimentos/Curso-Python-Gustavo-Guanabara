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

n = int(input("Digite um número de 0 a 20: \n"))
    
if n < 0 or n > 20:
    print("Digite um número entre 0 e 20")
else:
    print(f"Você digitou: {extensos[n]}!")