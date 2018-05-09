# Faça um programa que leia uma frase qualquer e mostre:
# Quantas vezes aparece a letra "a"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

# Faça um programa que leia uma frase qualquer:
frase = str(input("Digite uma frase: \n")).lower().strip()

# Tamanho total da string (só porque eu quero mesmo):
print("Tamanho total da string: {}".format(len(frase)))

# Quantas vezes aparece a letra "a":
print("A letra A aparece {} vezes na frase.".format(frase.count("a")))

# Em que posição ela aparece a primeira vez:
print("A primeira letra A aparece na posição {}.".format(frase.find("a")))

# Em que posição ela aparece a última vez:
print("A última letra A apareceu na posição {}.".format(frase.rfind("a")))
