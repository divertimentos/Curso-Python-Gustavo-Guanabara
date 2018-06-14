num = [2, 5, 9, 1]
num[2] = 3

# num[4] = 7
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
num.remove(2)  # Remove apenas o primeiro elemento, caso haja vários.
# num.pop(2)

if 5 in num:
    num.remove(5)
else:
    print("Não achei o número 5.")
print(num)
print(f"Esta lista tem {len(num)} elementos.")
 

valores = []
for cont in range(0, 5):
    valores.append(int(input("Digite um valor: \n")))

for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei: {v}")
print("Cheguei no final da lista.")


a = [2, 3, 4, 7]
b = a[:]  # Criar uma cópia de uma lista da forma correta
b[2] = 50

print(f"Lista {a}")
print(f"Lista {b}")
