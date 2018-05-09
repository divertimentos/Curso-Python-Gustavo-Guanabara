# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo

# Inclusive posso dizer qual tipo de triângulo pode ser formado.
# Não deve ser difícil isso em Python.

ab = float(input("Primeiro segmento de reta: \n"))
cd = float(input("Segundo segmento de reta: \n"))
ef = float(input("Terceiro segmento de reta: \n"))

if ab + cd > ef and ab + ef > cd and cd + ef > ab:
    print("O triângulo existe.")
else:
    print("O triângulo não pode existir.")
