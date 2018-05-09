frase = "Curso em Vídeo Python"
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])

# Imprimindo textos inteiros:

print(''''

Ausência

Eu deixarei que morra em mim o desejo de amar os teus olhos que são doces
porque nada te poderei dar senão a mágoa de me veres eternamente exausto
No entanto a tua presença é qualquer coisa como a luz e a vida
''')

print(frase.count("o"))
print(frase.count("O"))
print(frase.upper().count("O"))  # Jogou pra caixa alta e contou
print(len(frase))
print(len(frase.strip()))
print(frase.replace("Python", "Android"))
print("Curso" in frase)
print("Código do find:", frase.find("Vídeo"))
print(frase.lower().find("vídeo"))

dividido = (frase.split())
print(dividido[0])
print(dividido[2][3])
