n = s = 0
while True:
    n = int(input("Digite um inteiro: \n"))
    if n == -1:
        break
    s += n
# print("A soma vale {}.".format(s))

# f-string:

print(f"A soma vale: {s}")