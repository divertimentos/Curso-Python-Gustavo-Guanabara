''' Faça um programa que leia um número qualquer e mostre
o seu fatorial 

exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120
'''

num = int(input("Descubra o fatorial de um número: \n"))
counter = num
fat = 1

print("Calculando {}! = ".format(num), end="")
while counter > 0:
    print("{}".format(counter), end="")
    fat *= counter
    counter -= 1
    print(" x " if counter > 1 else " = ", end="")
print("{}".format(fat))
