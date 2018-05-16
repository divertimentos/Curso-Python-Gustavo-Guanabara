''' Crie um programa que leia vários números inteiros pelo teclado
No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valores lidos
O programa deve perguntar ao usuário se ele quer ou não continuar
a digitar valores
'''

flag = False
counter = adder = mean = highest = lowest = 0

while flag == False:
    n = int(input("Digite um número inteiro: \n"))

    #  Média:
    adder += n
    counter += 1
    mean = (adder / counter)

    #  Maior/Menor:
    if n > highest:
        highest = n
    if lowest == 0:
        lowest = n
    if n < lowest:
        lowest = n

    #  Continuação:
    cont = str(input("Quer continuar? [SIM / NÃO] \n")).strip().upper()
    if cont == "NÃO":
        flag = True

print("Média: {:.1f}".format(mean))
print("Maior: {} | Menor: {}".format(highest, lowest))
