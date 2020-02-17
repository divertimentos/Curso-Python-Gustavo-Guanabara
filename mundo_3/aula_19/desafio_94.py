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

personal_info = dict()
general_info = list()

while True:
    personal_info['nome'] = input("Nome: \n")
    personal_info['idade'] = input("Idade: \n")
    general_info.append(personal_info)


    leave = input("Continuar? [S / N] \n")
    if leave[0] == "N":
        break
print(general_info)

# while True:
#     name_dict['nome'] = input("Nome: \n")
    
#     sex = input("Sexo [M / F]: \n")
#     sex = sex[0:1].upper()
#     sex_dict['sex'] = sex
    
#     age_dict['age'] = input("Idade: \n")

#     people_list.append([name_dict, sex_dict, age_dict])
#     leave = input("Continuar? [S / N] \n")
#     if leave[0] == "N":
#         break

# print(general_list)