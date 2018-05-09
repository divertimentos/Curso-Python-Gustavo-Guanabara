# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "Santo"

city = input("Digite uma cidade: \n").lower().strip().split()
print(city[0] == "santo")
