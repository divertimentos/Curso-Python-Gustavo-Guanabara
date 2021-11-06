"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas 'aumentar()', 'diminuir()', 'dobro()' e 'metade()'.

Faça também um programa que importe esse módulo e use algumas dessas funções.

Obs.: por exemplo, o 'aumentar()' recebe o preço e uma porcentagem, e calcula.

o 'diminuir()', mesma coisa.

"""

import moeda

# input_usuario = float(input("Digite o preço: \n"))
input_usuario = 423

print(f"A metade de {input_usuario} é {moeda.metade(input_usuario)}")
print(f"O dobro de {input_usuario} é {moeda.dobro(input_usuario)}")
print(f"Aumentando 10%, temos {moeda.aumentar(input_usuario, 10)}")
print(f"Diminuindo 10%, temos {moeda.diminuir(input_usuario, 10)}")
