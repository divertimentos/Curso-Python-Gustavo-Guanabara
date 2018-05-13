'''
Melhore o exercício 61, perguntando para o usuário
se ele quer mostrar mais alguns termos
O programa encerra quando ele disser que quer mostrar "0 termos"
'''

prim = int(input("Primeiro termo: \n"))
raz = int(input("Razão da PA: \n"))

counter = 1
termo = 0
user = -1
tam = 10  # quantidade de loops (termos)

while True:
    while counter < tam:
        termo += raz
        counter += 1
        print(termo)
    user = int(input("Mais termos: \n"))

    if user == 0:
        break
    user += counter
    tam = user

print("Fim.")
