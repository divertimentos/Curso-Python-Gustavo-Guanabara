"""
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista.

No final, mostre:
a. Quantas pessoas foram cadastradas
b. A média de idade do grupo
c. uma lista com todas as mulheres
d. uma lista com todas as pessoas com idade acima da média.
"""

person_dict = dict()
general_info, names, names_quantity, ages, women, above_mean = list(), list(), list(), list(), list(), list()

while True:
    # recebe nome:
    person_dict['name'] = input("Nome: \n")

    # recebe sexo:
    sex = input("Sexo [M/F]: \n")
    sex = sex[0].upper()
    person_dict['sex'] = sex

    # recebe idade:
    person_dict['age'] = float(input("Idade: \n"))
    
    # insere os dicionários na lista:
    general_info.append(person_dict.copy())

    # continuar ou sair?
    leave = input("Continuar? [S/N] \n")
    leave = leave.upper()
    if leave[0] == "N":
        break

for dictionary in general_info:
    # a.: quantas pessoas foram cadastradas:
    names_quantity.append(dictionary.get("name"))

    # b.: a média de idade do grupo:
    ages.append(dictionary.get("age"))
    age_mean = sum(ages)/len(ages)

    # c.: uma lista com todas as mulheres:
    for key, value in dictionary.items():
        if value == "F":
            women.append(dictionary.get("name"))

    # d.: uma lista com todas as pessoas com idade acima da média:
    if dictionary.get("age") > (age_mean):
        above_mean.append(dictionary.get("name"))

print(f"Pessoas cadastradas: {len(names_quantity)}")
print(f"Idade média do grupo: {age_mean:.1f} anos.")
print(f"Mulheres do grupo: {women}")
print(f"Pessoas com idade acima da média: {above_mean}")
