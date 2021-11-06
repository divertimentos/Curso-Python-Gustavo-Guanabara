"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular
e o outro chamado show, que será um valor lógico (opcional) 
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""


def fatorial(num, show=False):
    """
    --> Calcula o fatorial de um número.
    :param num: o número a ser calculado
    :param show: (opcional) mostrar ou não a conta
    :return O valor do fatorial de um número num
    """
    fatorial = 1
    for i in range(num, 0, -1):
        if show:
            print(i, end="")
            if i > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
        fatorial *= i
    return fatorial


numero = int(input("Digite um número par saber o fatorial: \n"))
print(fatorial(numero, show=True))
