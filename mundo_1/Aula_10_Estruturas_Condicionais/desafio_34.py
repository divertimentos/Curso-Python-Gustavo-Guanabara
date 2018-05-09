'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento

Para salários superiores a R$ 1.250,00, calcule um aumento de 10%

Para os inferiores ou iguais, o aumento é de R$ 15%.
'''

sal = float(input("Digite seu salário: \n"))
if sal > 1250:
    aum = (sal + (sal * 10/100))
    print("Com o aumento de 10%, o seu salário foi de R${:.2f} para R${:.2f}.".format(sal, aum))
else:
    aum = (sal + (sal * 15/100))
    print("Com o aumento de 15%, o seu salário foi de R${:.2f} para R${:.2f}.".format(sal, aum))
