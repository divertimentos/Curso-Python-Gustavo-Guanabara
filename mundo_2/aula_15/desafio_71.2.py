from datetime import datetime

'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado(inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.

Obs.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

now = datetime.now().hour

num = int(input('''
Seja bem-vindo ao Banco Python!

Digite o valor que você deseja sacar: \nR$'''))

cedulas = [50, 20, 10, 1]
lista = []

print("\nSacando:")
while num > 0:
    for i in cedulas:
        cedulas = num // i
        num %= i

        if cedulas > 0:
            print(f"{cedulas} notas de R${i}")
            if num == 0:
                break

if now < 12:
    now = "um bom dia"
elif now < 19:
    now = "uma boa tarde"
elif now < 23:
    now = "uma boa noite"

print(f"\nTenha {now}. Até a próxima!")