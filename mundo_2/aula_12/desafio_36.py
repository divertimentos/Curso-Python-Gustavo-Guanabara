'''
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa
O programa vai perguntar o valor da casa, o salário do comprador e em quantos
anos ele vai pagar

Calcule o valor da prestação mensal,
sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado
'''
preco = float(input("Qual o valor da casa? \n"))
sal = float(input("Qual é o seu salário? \n"))
tempo = int(input("Em quantos anos você vai pagar? \n"))

mensalidade = (preco / (tempo * 12))
print("Valor da casa: {:.2f}".format(preco))
print("Prestação: {:.2f}".format(mensalidade))

if mensalidade >= (sal * 30 / 100):
    # if sal < (mensalidade * (30 / 100)):
    print("Empréstimo negado.")
else:
    print('''Empréstimo concedido.
    Mensalidade durante {} anos: R${:.2f}.'''.format(tempo, mensalidade))
