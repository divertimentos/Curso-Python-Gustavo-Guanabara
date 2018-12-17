# Aula de listas 2 (eu aprendi como sendo matrizes)

teste = list()
teste.append("Gustavo")
teste.append(40)

galera = list()
galera.append(teste[:])

teste[0] = "Destruidora de Mundos"
teste[1] = 9000
galera.append(teste[:])

print(galera)
'''

'''
galera = [["Kendrick Nanar", 30], ["Power Ranger Preto", 33], ["Senhora da Magia", 22], ["Sacerdotisa de Elennor", 23]]

for p in galera:
    print(f"{p[0]} tem {p[1]} anos.")

#### **** #### **** ####

galera = list()
dado = list()
totmai = totmen = 0

for i in range(0, 3):
    dado.append(str(input("Dĩgite um nome: \n")))
    dado.append(int(input("Digite uma idade: \n")))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade")
        totmai += 1
    else:
        totmen += 1

print(f"Temos {totmai} maiores e {totmen} menores.")
