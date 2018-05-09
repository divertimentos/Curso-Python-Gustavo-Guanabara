# Faça um programa que calcule a soma entre todos os números impares
# que são múltiplos de três (3) e que se encontram no intervalo de 1 até 500.

s = 0  # Contador de soma
for num in range(1, 501):  # de 1 até 500
    if num % 2 != 0:  # Ímpares
        if num % 3 == 0:  # Ímpares múltiplos de 3
            s += num  # soma = soma + num
print("A soma dos múltiplos é: {}.".format(s))
