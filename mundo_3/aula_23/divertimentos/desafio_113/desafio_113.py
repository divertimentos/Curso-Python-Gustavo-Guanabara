"""Reescreva a função `leiaInt()` que fizemos no desafio 104,
incluindo agora a possobilidade da digitação de um número de tipo inválido.
Aproveite e crie também a função `leiaFloat()` com a mesma funcionalidade."""

from os import system

system("clear")


def leia_int(message):
    while True:
        try:
            number = int(input(message))
        except (ValueError, TypeError):
            print("\033[0;31mERRO! Digite um número INTEIRO válido!\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[0;31mUsuário preferi não digitar esse número\033[m")
            return 0
        else:
            return number


def leia_float(message):
    while True:
        try:
            number = float(input(message))
        except (ValueError, TypeError):
            print("\033[0;31mERRO! Digite um número REAL válido!\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[0;31mUsuário preferiu não digitar esse número\033[m")
            return 0
        else:
            return number


user_int_num = leia_int("Digite um número INTEIRO: \n")
user_float_num = leia_int("Digite um número REAL: \n")

print(f"""O valor digitado foi de {
      user_int_num} e o real foi de {user_float_num}.""")
