n1 = float(input("Digite a primeira nota: \n"))
n2 = float(input("Digite a segunda nota: \n"))

m = ((n1 + n2) / 2)
print("A sua média foi {:.1f}".format(m))

# Método tradicional:

# if m >= 6.0:
#    print("Sua média foi boa. Parabéns")
# else:
#    print("Sua média foi ruim! Estude mais!")

# Método simplificado:
print("Parabéns!" if m >= 6.0 else "Estude mais!")
