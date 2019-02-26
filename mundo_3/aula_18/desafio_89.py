"""
Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta.

No final, mostre um boletim contendo a média de cada um
e permita que o usuário possa mostrar as notas de cada aluno individualmente

"""


"""
Cria um programa que lê nome e duas notas de vários alunos
e guarda-os numa lista completa.
"""

from statistics import mean

infos_students = list()


def get_name():
    return input("Nome do aluno: \n")


def get_grades(student_name):
    grades = list()
    counter = 1
    grades.append(student_name)
    while counter < 3:
        grade = int(input(f"{counter}ª nota: \n"))
        grades.append(grade)
        counter += 1
    infos_students.append(grades)
    return infos_students


def display_infos():
    return infos_students


while True:
    get_grades(get_name())
    question = input("Deseja adiciona mais um aluno? \n").lower()
    if question[0] == "n":
        # print(display_infos())
        break

"""
Mostra um boletim contendo a média de cada um 
e permita que o usuário possa mostrar as notas de cada aluno individualmente
"""


def calculate_mean(students_infos):
    students_means = list()
    new_infos = list()  # bad naming

    for item in students_infos:
        students_means.append(item[0])
        students_means.append(mean(item[1:]))
        new_infos.append(students_means)
        del students_means
        students_means = list()

    return new_infos


def display_school_report():
    pass


# display_school_report(display_infos())

print(calculate_mean(display_infos()))
