'''
Crie um programa onde o usuário digite uma expressão qualquer
que use parênteses.
Seu aplicativo deverá analisar se a expressão passada 
está com os parênteses abertos e fechados na ordem correta.
'''

lista = []
x = 0  # Contador
exp = str(input("Digite uma expressão: \n"))
print(f"Tamanho da expressão: {len(exp)}")

while x < len(exp):
    if exp[x] == "(":
        lista.append(exp[x])
    if exp[x] == ")":
        if len(lista) > 0:
            del lista[-1]
            del x
    x += 1
print(f"Lista: {lista}")

'''
while x < len(exp):
    if exp[x] == "(":
        lista.append(x)
    if exp[x] == ")":
        if len(lista) > 0:
<<<<<<< HEAD
            lista = lista.pop(lista[-1])
    x += 1

print(f"lista: {lista}")
'''
=======
            lista = lista.pop(lista[-1]
>>>>>>> a2932aef63ceeed5807e26dcd9562ef5e1e4ba21
