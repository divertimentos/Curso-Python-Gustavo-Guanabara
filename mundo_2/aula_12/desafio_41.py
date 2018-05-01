'''
A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- até 9 anos: mirim
- até 14 anos: infantil
- até 19 anos: júnior
- até 20 anos: sênior
acima de 20: master
'''
idade = int(input("Digite sua idade: \n"))

if idade < 10:
    print("Mirim: {} anos.".format(idade))
elif idade < 15:
    print("Infantil: {} anos.".format(idade))
elif idade < 20:
    print("Júnior: {} anos.".format(idade))
elif idade < 21:
    print("Sênior: {} anos.".format(idade))
else:
    print("Master: {} anos.".format(idade))
