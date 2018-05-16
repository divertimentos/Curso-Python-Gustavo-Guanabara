'''
Crie um programa que leia vários números inteiros pelo teclado
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada

No final, mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando o flag!)
'''

flag = False
somador = 0
counter = 0

while flag == False:
    num = int(input("Digite um número [999 para parar]: \n"))
    if num == 999:
        flag = True
    else:
        somador += num
        counter += 1
print("Soma: {}.".format(somador))
print("Números digitados: {}.".format(counter))
