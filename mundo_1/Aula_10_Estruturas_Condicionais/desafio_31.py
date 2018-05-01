'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200km
e R$ 0,45 para viagens mais longas
'''
dist = int(input("Qual a distância a ser percorrida? \n"))
if dist <= 200:
    price = (dist * 0.50)
    print("Preço da passagem: R${:.2f}.".format(price))
else:
    price = (dist * 0.45)
    print("Preço da passagem: R$ {:.2f}.".format(price))
