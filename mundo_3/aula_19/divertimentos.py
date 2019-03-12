dados = dict()
dados = {"nome": "Pedro", "idade": 25}

dados["sexo"] = "M"
print(dados)

del dados["idade"]
print(dados)

star_wars = {
    "titulo": "Star Wars",
    "ano": 1977,
    "diretor": "George Lucas",
}

avengers = {
    "titulo": "Avengers",
    "ano": 2012,
    "diretor": "Joss Whedon",
}

locadora = [star_wars, avengers]

print(locadora[0]["ano"])
print(locadora[1]["titulo"])

# print(filme.values())
# print(filme.keys())
# print(filme.items())

# for k, v in filme.items():
#     print(f"O {k} é {v}")

pessoas = {"nome": "Gustavo", "sexo": "M", "idade": 22}
pessoas["peso"] = 98.5

for k, v in pessoas.items():
    print(f"{k} = {v}")

brasil = list()
estado1 = {"uf": "Rio de Janeiro", "sigla": "RJ"}
estado2 = {"uf": "São Paulo", "sigla": "SP"}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]["uf"])


estado = dict()
brasil = list()

for c in range(0, 3):
    estado["uf"] = str(input("Unidade Federativa: \n"))
    estado["sigla"] = str(input("Sigla do Estado: \n"))
    brasil.append(estado.copy())

for estado in brasil:
    for k, v in estado.items():
        print(f"O campo {k} tem valor {v}.")
