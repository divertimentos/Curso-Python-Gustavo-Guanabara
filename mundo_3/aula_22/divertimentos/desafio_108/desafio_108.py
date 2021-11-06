"""
Adapte o código do desafio 107, criando uma função adicional chamada 'moeda()' que consiga mostrar os valores como um valor monetário formatado.
"""

import moeda

# input_usuario = float(input("Digite o preço: \n"))
input_usuario = 423

print(f"A metade de R$ {input_usuario} é {moeda.moeda(moeda.metade(input_usuario))}")
print(f"O dobro de R$ {input_usuario} é {moeda.moeda(moeda.dobro(input_usuario))}")
print(f"Aumentando 10%, temos {moeda.moeda(moeda.aumentar(input_usuario, 10))}")
print(f"Diminuindo 10%, temos {moeda.moeda(moeda.diminuir(input_usuario, 10))}")
