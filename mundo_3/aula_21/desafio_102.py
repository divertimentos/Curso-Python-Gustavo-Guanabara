"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular
e o outro chamado show, que será um valor lógico (opcional) 
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""

def fatorial(num, show=False):
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

print(fatorial(5, show=True))