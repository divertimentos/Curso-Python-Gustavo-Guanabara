'''
Refaça o DESAFIO 35, dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:

- equilátero: todos os lados iguais
- isósceles: dois lados iguais
- escaleno: todos os lados diferentes
'''
a = float(input("Primeiro segmento de reta: \n"))
b = float(input("Segundo segmento de reta: \n"))
c = float(input("Terceiro segmento de reta: \n"))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("O triângulo existe.")
    if a == b == c:
        print("Triângulo Equilátero.")
    elif (a == b) or (a == c) or (b == c):
        print("Triângulo Isósceles.")
    else:
        print("Triângulo escaleno.")
else:
    print("O triângulo inexiste.")
