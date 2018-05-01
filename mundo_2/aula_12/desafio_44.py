'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando
o seu preço normal, e condição de pagamento:

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

if forma == 1:
    print("Você selecionou à vista no dinheiro.")
    print("Este é o valor a se pago.")
elif forma == 2:
    print("Você selecionou à vista no cartão.")
elif forma == 3:
    print("Você selecionou em 2x no cartão.")
elif forma == 4:
    print("Você selecionou em 3x ou mais no cartão.")
else:
    print("Por favor, selecione uma alternativa válida. Tente novamente.")
