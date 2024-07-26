"""Reescreva a função `leiaInt()` que fizemos no desafio 104,
incluindo agora a possobilidade da digitação de um número de tipo inválido.
Aproveite e crie também a função `leiaFloat()` com a mesma funcionalidade."""


def leia_int(entrada_usuario):
    is_ok = False
    value = None
    while True:
        numero = input(f"{entrada_usuario} \n")
        if numero.isnumeric():
            value = numero
            is_ok = True
        else:
            print("\033[0;31mERRO! Digite um número inteiro válido!\033[m")
        if is_ok:
            break
    return value
