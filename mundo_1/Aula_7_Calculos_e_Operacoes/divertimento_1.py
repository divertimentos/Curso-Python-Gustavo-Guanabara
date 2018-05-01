nome = "Mitsurugi"
print("Prazer em te conhecer, {:20}!".format(nome))
print("Prazer em te conhecer, {:>20}!".format(nome))
print("Prazer em te conhecer, {:<20}!".format(nome))
print("Prazer em te conhecer, {:^20}!".format(nome))
print("Prazer em te conhecer, {:=^20}!".format(nome))

n1 = int(input("Um valor: \n"))
n2 = int(input("Outro valor: \n"))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print("A soma é {}, \no produto é {} \ne a divisão é {:.3f}".format(s, m, d), end=" ")
print("\nDivisão inteira: {} \ne potência: {}.".format(di, e))
