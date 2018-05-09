# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

n = float(input("Digite o preço de um produto: \nR$"))
desconto = n * 5 / 100
print("Na liquidação da loja, esse produto de R${:.2f} está com desconto de 5%, \nou seja, vai custar só R${:.2f}.".format(n, n - desconto))
