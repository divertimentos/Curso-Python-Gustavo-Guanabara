'''
Crie um programa onde o usuário digite uma expressão qualquer
que use parênteses.
Seu aplicativo deverá analisar se a expressão passada 
está com os parênteses abertos e fechados na ordem correta.
'''

lista = []
exp = str(input("Digite uma expressão: \n"))
x = 0  # Contador

while x < len(exp):
    if exp[x] == "(":
        lista.append(x)
    if exp[x] == ")":
        if len(lista) > 0:
            lista = lista.pop(lista[-1])
        