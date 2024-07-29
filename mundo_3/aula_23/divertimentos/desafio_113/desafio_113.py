"""Reescreva a função `leiaInt()` que fizemos no desafio 104,
incluindo agora a possobilidade da digitação de um número de tipo inválido.
Aproveite e crie também a função `leiaFloat()` com a mesma funcionalidade."""

from os import system

system("clear")


# def leia_int_old(entrada_usuario):
#     is_ok = False
#     value = None
#     while True:
#         numero = input(f"{entrada_usuario} \n")
#         if numero.isnumeric():
#             value = numero
#             is_ok = True
#         else:
#             print("\033[0;31mERRO! Digite um número inteiro válido!\033[m")
#         if is_ok:
#             break
#     return value


def leia_int_new():
    is_ok = False
    int_final_value = None
    float_final_value = None
    while True:
        integer_user_input = input("Digite um número inteiro (int): \n")
        float_user_input = float("Digite um número Real (float): \n")
        try:
            int(integer_user_input)
            float(float_user_input)
            int_final_value = integer_user_input
            float_final_value = float_user_input

            is_ok = True
        except ValueError:
            print("\033[0;31mERRO! Digite um número inteiro válido!\033[m")

        else:
            if is_ok:
                break
    return f"""O valor inteiro digitado foi {int_final_value}
    e o real foi {float_final_value}"""


# number = leia_int_old("Digite um número:")
# print(f"Você acabou de digitar o número: {number}.")


print(leia_int_new())
