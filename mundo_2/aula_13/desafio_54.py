from datetime import date
''' Crie um programa que leia o ano de nascimento de sete pessoas
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores'''
atual = date.today().year
counter = 0
for i in range(7):
    num = int(input("Digite anos de nascimento: \n"))
    if atual - num >= 21:
        counter += 1
print("Das 7 pessoas, {} são maiores de 21 anos.".format(counter))
