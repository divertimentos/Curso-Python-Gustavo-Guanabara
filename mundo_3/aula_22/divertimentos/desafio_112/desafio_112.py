"""
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. 
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), 
mas com uma validação de dados para aceitar apenas valores que sejam monetários.
"""

from utilidadescev import moeda
from utilidadescev import dado


input_usuario = dado.leiaDinheiro("Digite o preço: \n")

print(moeda.resumo(input_usuario, 20, 12))
