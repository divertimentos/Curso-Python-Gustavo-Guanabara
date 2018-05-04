''' Refaça o desafio 009, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for'''

num = int(input("Digite um número: \n"))
counter = 1
for i in range(0, 10):
    print("{} x {} = {}".format(num, counter, (num * counter)))
    counter += 1
