# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input("Digite seu salário: \nR$"))
aumento = salario * 15/100
print("O salário do funcionário, que é de R${:.2f}, vai subir para R${:.2f} com o aumento de 15%.".format(salario, salario + aumento))
