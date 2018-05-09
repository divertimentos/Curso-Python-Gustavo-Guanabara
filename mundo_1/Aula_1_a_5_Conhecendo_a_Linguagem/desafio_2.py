# Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada

ano = int(input("Ano de nascimento: \n"))
mes = int(input("Mês de nascimento: \n"))
dia = int(input("Dia de nascimento: \n"))

print("A pessoa nasceu em: {}/{}/{}".format(dia, mes, ano))
print("A pessoa nasceu no dia {} do mês {} do ano de {}.".format(dia, mes, ano))
