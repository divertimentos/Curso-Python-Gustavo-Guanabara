# TESTES DE CÓDIGO NO VISUAL CODE STUDIO

from random import randint

name = input(str("Digite seu nome: \n"))
# print(name)
print("Olá, {}.".format(name))


contador = 0
lista = "Paralelepípedo"
for i in lista:
    print(lista[contador])
    contador += 1

#  Teste de erro de pep.


ran = randint(1, 50)
print("Teste de número randômico: {}.".format(ran))

print("Eu escolho vc, {}.".format(name))
print("Eu escolho você, {}.".format(ran))
print("Estrelas na chuva são: {}.".format(ran))

# Código de teste escrito no Vim:

vim = "print feito no vim caraio"

vim = vim.split()
print(vim)
for i in vim:
    print(i)
