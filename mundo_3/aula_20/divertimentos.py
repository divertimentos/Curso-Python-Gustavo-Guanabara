def lin():
  print('-' * 30)
lin()

# Programa principal
print("Curso em Vídeo")
lin()
print("Aprenda Python")
lin()
print("Gustavo Guanabara")
def escreve_mensagem(mensagem):
    print("-" * 30)
    print(mensagem)
    print("-" * 30)
escreve_mensagem("Sistema de Alunos")
escreve_mensagem("Cadastro de Funcionários")
escreve_mensagem("Erro do Sistema")
# EXEMPLOS NA PRÁTICA
a = 5
b = 4
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)
a = 2
b = 1
s = a + b
print(s)


def soma(a, b):
    s = a + b
    print(s)

# # Programa principal
# soma(4, 5)
# soma(8, 9)
# soma(2, 1)

def subtracao(a, b):
    print(f"A = {a} e B = {b}")
    s = a-b
    print(f"A subtração A-B = {s}")

subtracao(a=10, b=5)  # resp.: 5
subtracao(b=10, a=5)  # resp.: -5

def contador(*num):
    print(f"Recebi os valores {num} e eles são {len(num)}")
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
