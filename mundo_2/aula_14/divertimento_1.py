'''
r = "S"
n = 1
while r == "S":
    n = int(input("Digite um valor: \n"))
    r = str(input("Quer continuar? [S/N] \n")).upper()
print("Você digitou {}, que é a condição de parada.".format(r))
'''

even = 0
odd = 0
n = 1

while n != 0:
    n = int(input("Digite um valor: \n"))
    if n != 0:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
print("Pares {}".format(even))
print("Ímpares {}.".format(odd))
