''' Faça um programa que leia o peso de cinco pessoas
No final, mostre qual foi o maior e o menor peso lidos'''

larger = 0
smaller = 0

for i in range(1, 6):
    weight = float(input("Digite um peso: \n"))
    if i == 1:
        larger = weight
        smaller = weight
    else:
        if weight > larger:
            larger = weight
        elif weight < smaller:
            smaller = weight

print("O maior peso é {}kg".format(larger))
print("O menor peso é {}kg.".format(smaller))
