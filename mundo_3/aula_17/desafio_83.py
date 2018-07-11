'''
Crie um programa onde o usuário digite uma expressão qualquer
que use parênteses.
Seu aplicativo deverá analisar se a expressão passada 
está com os parênteses abertos e fechados na ordem correta.
'''

lista = []
exp = str(input("Digite uma expressão: \n"))

for simb in exp:
    if simb == "(":
        lista.append(simb)
    elif simb == ")":
        if len(lista) > 0:
            lista.pop(-1)
        else:
            lista.append(")")
            break

print(f"Lista: {lista}")

if len(lista) == 0:
    print("Válido")
else:
    print("Inválido")
