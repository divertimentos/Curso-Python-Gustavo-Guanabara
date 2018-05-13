''' Crie um programa que leia dois valores e mostre um menu
na tela:

1: somar
2: multiplicar
3: maior
4: novos números
5: sair do programa

Seu programa deverá realizar a operação solicitada em cada caso '''

num1 = float(input("Digite um número (1/2): \n"))
num2 = float(input("Digite outro número (2/2): \n"))
menu = (
'''\nMENU PRINCIPAL:
[1] soma
[2] multiplicação
[3] maior ou menor
[4] escolher novos números
[5] encerrar o programa\n '''
)
maior = 0
menor = 0

print(menu)

user = int(input("Sua escolha (opções de 1 a 5): \n"))
while user != 5:
    if user > 5:  # exceção maior
        print("Warning: escolha um número de 1 a 5.")
        user = int(input("Sua escolha: \n"))
    elif user < 0:  # exceção menor
        print("Warning: escolha um número positivo.")
        user = int(input("Sua escolha: \n"))
    else:  # Acionamento normal do programa:
        if user == 1:  # Soma:
            print("Vocẽ escolheu soma!")
            print("Resultado da soma: \n{} + {} = {}".format(num1, num2, (num1 + num2)))
            print(menu)
            user = int(input("Sua escolha: \n"))
        elif user == 2:  # Multiplicação:
            print("Você escolheu multiplicação!")
            print("Resultado da multiplicação: \n{} x {} = {:.0f}".format(num1, num2, (num1 * num2)))
            print(menu)
            user = int(input("Sua escolha: \n"))
        elif user == 3:  # Maior ou menor:
            if num1 > num2:
                maior = num1
                menor = num2
                print("O maior é {} e o menor é {}.".format(maior, menor))
                print(menu)
            elif num2 > num1:
                maior = num2
                menor = num1
                print("O maior é {} e o menor é {}.".format(maior, menor))
                print(menu)
            else:
                print("Os dois números são idênticos.")
                print(menu)
            user = int(input("Sua escolha: \n"))
        elif user == 4:  # Novos números:
            new_num1 = float(input("Novo número 1: \n"))
            new_num2 = float(input("Novo número 2: \n"))
            num1 = new_num1
            num2 = new_num2
            print(menu)
            user = int(input("Sua escolha: \n"))
print("Opção 5: programa encerrado.")
