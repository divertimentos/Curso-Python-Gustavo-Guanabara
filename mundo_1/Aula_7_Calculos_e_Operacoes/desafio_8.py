# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

n = int(input("Digite um valor em metros: \n"))
# print("{} metro(s), convertido(s) em centímetros, é {}cm; convertido(s) em milímetros é {}mm.".format(n, (n*100), (n*1000)))

print("{} metros são {} kilômetros.".format(n, n * 1000))
print("{} metros são {} hectômetros.".format(n, n * 100))
print("{} metros são {} decâmetros.".format(n, n * 10))

print("{} metros são {} metros.".format(n, n * 1))

print("{} metros são {} decímetros.".format(n, n / 10))
print("{} metros são {} centímetros.".format(n, n / 100))
print("{} metros são {} milímetros.".format(n, n / 1000))
