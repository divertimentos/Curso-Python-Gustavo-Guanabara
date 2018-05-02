'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal, e condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- em 3x ou mais no cartão: 20% de juros
'''
valor = float(input("Qual o preço do produto? \n"))
print("Selecione uma forma de pagamento")
print('''
Digite 1: Para pagar à vista no dinheiro.
Digite 2: Para pagar à vista no cartão.
Digite 3: Em 2x no cartão.
Digite 4: Em 3x no cartão ou mais \n''')
forma = int(input("Selecione a forma de pagamento: \n"))

if forma == 1:  # 10% de desconto
    print("Você selecionou à vista no dinheiro.")
    desconto = (valor * (10/100))
    print("Valor à vista no dinheiro: R${:.2f}.".format(
        valor - desconto))
elif forma == 2:  # 5% de desconto
    print("Você selecionou à vista no cartão.")
    desconto = (valor * (5 / 100))
    print("Valor à vista no cartão: {:.2f}.".format(valor - desconto))
elif forma == 3:  # Em até 2x no cartão: preço normal
    print("Você selecionou em 2x no cartão.")
    print("Pagamento à vista R$ {:.2f} ou em 2x de R${:.2f}.".format(
        valor, (valor / 2)))
elif forma == 4:  # Em até 3x ou mais: 20% de juros
    print("Você selecionou em 3x ou mais no cartão.")
    desconto = (valor * (30 / 100))
    print('''
    Pagamento, com juros de 30%, em:
    3x de R${:.2f}
    4x de R${:.2f}
    5x de R${:.2f}
    6x de R${:.2f}
    7x de R${:.2f}
    '''.format((valor + desconto) / 3, (valor + desconto) / 4, (valor + desconto) / 5, (valor + desconto) / 6, (valor + desconto) / 7))
else:
    print("Por favor, selecione uma alternativa válida. Tente novamente.")
