# Tuplas:

# TUPLAS SÃO IMUTÁVEIS

lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim", "Batata Frita")

print(lanche)
print(lanche[1]) #suco
print(lanche[-2]) #pizza
print(lanche[1:3]) #suco e pizza
print(lanche[2:]) # pizza até o final
print(lanche[:2]) # Hambúrguer e suco
print(lanche[-2:]) #Pizza, pudim
print(lanche[-3:]) # suco, pizza e pudim

# É impossível atribuir elementos às tuplas,
# a não ser no momento da declaração.


for comida in lanche:
    print(f"Eu vou comer {comida}")
print("Comi pra caramba.")


for cont in range(0, len(lanche)):
    print(lanche[cont])



for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")



print(sorted(lanche))



a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b  # A soma concatena as tuplas
print(c)
print(len(c))  # Tamanho da tupla nova
print(c.count(5))  # Quantas vezes aparece o  número 5
print(c.index(8))  # Em que posição está o número 8

pessoa = ("Gustavo", 39, "M", 99.88)
del(pessoa)
