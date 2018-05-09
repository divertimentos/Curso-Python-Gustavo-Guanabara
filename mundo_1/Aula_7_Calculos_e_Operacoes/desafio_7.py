# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

nota1 = float(input("Nota 1: \n"))
nota2 = float(input("Nota 2: \n"))
print("A média das notas {:.1f} e {:.1f} é {:.1f}!".format(nota1, nota2, ((nota1 + nota2) / 2)))
