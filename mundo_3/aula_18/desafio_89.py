'''
Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta.

No final, mostre um boletim contendo a média de cada um
e permita que o usuário possa mostrar as notas de cada aluno individualmente


'''

infos_alunos = list()


def get_name():
    name = input("Nome do aluno: \n")
    return name


def get_grades(student_name):
    grades = list()
    counter = 1
    grades.append(student_name)
    while counter < 3:
        grade = int(input(f"Nota {counter}: \n"))
        grades.append(grade)
        counter += 1
    return grades


print(get_grades(get_name()))
