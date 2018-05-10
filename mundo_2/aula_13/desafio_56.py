''' Desenvolva um programa que leia nome, idade e sexo de 4 pessoas
No final do programa, mostre:
 - A média de idade do grupo
 - Qual é o nome do homem mais velho
 - Quantas mulheres têm menos de 20 anos
 '''

mean = 0
counter = 0
adder = 0
add_age = 0
older = 0
name_older = ""

for i in range(2):
    name = str(input("Nome: \n"))
    age = int(input("Idade: \n"))
    sex = str(input("Sexo [M/F]: \n")).strip().upper()
    if sex == "M":
        if age > older:
            older = age
            name_older = name
    elif sex == "F":
        if age < 20:
            add_age += 1

    counter += 1
    adder += age
    mean = (adder / counter) 

print("A média de idade do grupo é de {} anos.".format(mean))
print("O nome do homem mais velho é {} e ele tem {} anos".format(
    name_older, older))

if add_age == 0:
    print("Nenhuma mulher tem menos de 20 anos.")
elif add_age == 1:
    print("{} mulher tem menos de 20 anos.".format(add_age))
elif add_age >= 2:
    print("{} mulheres têm menos de 20 anos.".format(add_age))