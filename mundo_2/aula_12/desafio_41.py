from datetime import date
'''
A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- até 9 anos: mirim
- até 14 anos: infantil
- até 19 anos: júnior
- até 20 anos: sênior
acima de 20: master
'''
atual = date.today().year
nasc = int(input("Ano de nascimento do(a) nadador(a): \n"))
idade = atual - nasc
print("O atleta tem {} anos em {}.".format(idade, atual))


if idade <= 9:
    print("Classificação: Mirim.".format(idade))
elif idade <= 14:
    print("Classificação: Infantil.".format(idade))
elif idade <= 19:
    print("Classificação: Júnior.".format(idade))
elif idade <= 25:
    print("Classificação: Sênior.".format(idade))
else:
    print("Classificação: Master.".format(idade))
