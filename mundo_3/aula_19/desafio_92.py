"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-os (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de zero, o dicionário receberá também
o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos
a pessoa vai se aposentar.

Obs.: aposentadoria em 35 anos de contribuição.
"""

worker_infos = dict()

name = input("Digite um nome: \n")
birthday = input("Data de nascimento: \n")
ctps = int(input("Número da carteira de trabalho (CTPS): \n"))

retirement_age = int()
age = int()


worker_infos["name"] = name
worker_infos["birthday"] = birthday
worker_infos["ctps"] = ctps

if ctps != 0:
    hiring_date = input("Data de contratação: \n")
    salary = int(input("Salário: \nR$ "))
    
    worker_infos["hiring date"] = hiring_date
    worker_infos["salary"] = salary

print(worker_infos)
