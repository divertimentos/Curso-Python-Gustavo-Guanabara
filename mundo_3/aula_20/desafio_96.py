"""Faça um programa que tenha uma função chamada area(), que receba dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno
"""
def cabecalho(titulo):
    print("-" * len(titulo))
    print(f"{titulo}")
    print("-" * len(titulo))

cabecalho("Controle de Terrenos")

def area(largura, comprimento):
    print(f"A área de um terreno '{largura}x{comprimento}' é de {largura * comprimento}m².")

largura = float(input("Largura (m): \n"))
comprimento = float(input("Comprimento: \n"))



area(largura, comprimento)