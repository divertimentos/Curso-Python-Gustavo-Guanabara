# from datetime import date
'''
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
'''
num = int(input("Descubra se um ano é bissexto: \n"))

if num % 4 == 0:
    str_num = str(num)
    if str_num[-2:] == "00":  # Só não chamo isso de gambiarra porque é elegante demais
        if num % 400 == 0:
            print("{} é bissexto.".format(num))
        else:
            print("{} não é bissexto.".format(num))
    else:
        print("{} é bissexto.".format(num))
else:
    print("{} não é bissexto.".format(num))
