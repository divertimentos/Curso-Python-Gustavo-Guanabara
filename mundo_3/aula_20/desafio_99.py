from time import sleep


"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

def lin():
  print('-' * 30)
lin()


def maior(*args):
    maior = 0
    print("Analisando os valores passados...")
    print("Valores informados: ", end="")
    for i in args:
        print(f"{i} ", end="")
        sleep(0.2)
    print("")
    print(f"Ao todo são {len(args)} valores.")
    
    if len(args) == 0:
      print(f"O maior valor informado foi {maior}")
    else:
      maior = max(args)
      print(f"O maior valor informado foi {maior}")
    lin()
    print("")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()