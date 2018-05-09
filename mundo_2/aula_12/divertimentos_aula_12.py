nome = str(input("Digite um nome: \n")).strip().lower().capitalize()

if nome == "Guilherme" or nome == "Kendrick":
    print("{} é um nome bonito.".format(nome))
elif nome == "Mateus" or nome == "Marcos":
    print("{} é um nome bem bíblico.".format(nome))
elif nome == "Galadriel" or nome == "Glorfindel":
    print("{} é um nome bem élfico.".format(nome))
else:
    print("Seu nome é bem normal.")
print("Tenha um excelente dia, {}.".format(nome))
