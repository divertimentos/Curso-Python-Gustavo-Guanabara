"""
Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), 
desenvolvido no desafio 108.
"""

import moeda

# input_usuario = float(input("Digite o preço: \n"))
input_usuario = 200

print(f"A metade de R$ {input_usuario} é {moeda.metade(input_usuario, True)}")
print(f"O dobro de R$ {input_usuario} é {moeda.dobro(input_usuario, True)}")
print(f"Aumentando 10%, temos {moeda.aumentar(input_usuario, 10, True)}")
print(f"Diminuindo 10%, temos {moeda.diminuir(input_usuario, 10, True)}")
