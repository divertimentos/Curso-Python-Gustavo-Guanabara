from datetime import date

"""
Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa tem voto 
NEGADO, OPCIONAL ou OBRIGATORIO nas eleições.
"""


def voto(birthyear):
    current_year = date.today().year
    age = current_year - birthyear
    if age < 16:
        return f"Com {age} anos de idade: VOTO NEGADO"
    elif age < 18 or age >= 65:
        return f"Com {age} anos de idade: VOTO OPCIONAL"
    elif age < 65:
        return f"Com {age} anos de idade: VOTO OBRIGATÓRIO"


ano_nasc = int(input("Em qual ano você nasceu? \n"))
print(voto(ano_nasc))
