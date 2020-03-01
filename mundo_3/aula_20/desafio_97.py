"""Faça um programa que tenha uma função chamada escreva(), 
que receba um texto qualquer como parâmetro 
e mostre uma mensagem com tamanho adaptável.

Ex:
escreva("Olá, Mundo!")

Saída:

~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~
"""

def escreva(texto):
    print("~" * len(texto))    
    print(f"{texto:^5}")
    print("~" * len(texto))    

escreva("Gustavo Guanabara")
escreva("Curso de Python no YouTube")
escreva("CeV")