'''
Faça um programa que leia o ano de nascimento de um jovem e informe
de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo
'''
from datetime import datetime

nasc = int(input("Em qual ano você nasceu? \n"))
ano_atual = datetime.now().year
# print("Ano atual: {}".format(ano_atual))
idade = (ano_atual - nasc)
if idade < 18:
    print("Você tem {} anos e vai se alistar daqui a {} anos.".format(idade, (18 - idade)))
elif idade > 18:
    print("Você tem {} anos e já passou seu período de alistamento.".format(idade))
    print("Se não se alistou, deveria ter se alistado há {} anos atrás.".format(idade - 18))
else:
    print("Você tem {} anos. Está na hora de se alistar.".format(idade))
