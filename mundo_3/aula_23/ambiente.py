from os import system
system('clear')

# Exemplo 1
# print(x)


# Exemplo 2
# n = int(input("Num: \n"))
# print(f"Você digitou o número {n}.")

# Exemplo 3
a = int(input("Numerador: \n"))
b = int(input("Demoninador: \n"))

try:
    r = a/b
except (ValueError, TypeError):
    print("Tivemos um problema com os tipos de dados digitados")
except ZeroDivisionError:
    print("Não é possível dividir um número por zero.")
    print(f"O resultado, então, é {a}.")

except Exception as error:
    print(f"O erro encontrado foi {error.__class__}")
else:
    print(f"O resultado é {r:.1f}")
finally:
    print("\nVolte sempre! Muito obrigado!")
