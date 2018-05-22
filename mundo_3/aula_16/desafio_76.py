'''
Crie um programa que tenha uma tupla única
com nomes de produtos e seus respectivos precos,
na sequência

No final, mostre uma listagem de precos,
organizando os dados em forma tabular
'''

listagem = ("pão", 1, "leite", 3.50, "frango", 10.90)

print("=" * 35)
print("Pau no cu da interface, na moralzinha.")
print("=" * 35)

produto = 0
preco = 1

for item in range(0, len(listagem)// 2):
    print(f"{listagem[produto]} ***** R${listagem[preco]}")
    preco += 2
    produto += 2

# Esse é o programa mais gambiarrilson que eu já fiz, mas funcionou.