"""
Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.

No final, mostre o conteúdo da estrutura na tela.
"""

student_info = dict()

student_info["nome"] = str(input("Nome do aluno: \n"))
student_info["media"] = float(input("Insira a média: \n"))

print(student_info)