# def lin():
#   print('-' * 30)

# lin()
# # Programa principal
# print("Curso em Vídeo")
# lin()
# print("Aprenda Python")
# lin()
# print("Gustavo Guanabara")

# def escreve_mensagem(mensagem):
#     print("-" * 30)
#     print(mensagem)
#     print("-" * 30)

# escreve_mensagem("Sistema de Alunos")
# escreve_mensagem("Cadastro de Funcionários")
# escreve_mensagem("Erro do Sistema")

# # EXEMPLOS NA PRÁTICA
# a = 5
# b = 4
# s = a + b
# print(s)

# a = 8
# b = 9
# s = a + b
# print(s)

# a = 2
# b = 1
# s = a + b
# print(s)


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
