''' Crie um programa que leia vários números inteiros pelo teclado
O programa só vai parar quando o usuário digitar 999,
que é a condição de parada (flag).
No final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando o flag)
'''
soma = counter = 0
while True:
    n = int(input("Digite inteiros [999 para parar] \n"))
    if n == 999:
        break
    else:
        counter += 1
        soma += n
print(f"Foram digitados {counter} números")
print(f"A soma entre eles é: {soma}")
