def dobro(num):
    return num * 2


def metade(num):
    return num / 2


def aumentar(num, taxa):
    resultado = num + (taxa * num / 100)
    return resultado


def diminuir(num, taxa):
    resultado = num - (taxa * num / 100)
    return resultado


def moeda(num):
    num_string = str(num)
    splitted_num = num_string.split(".")
    parte_inteira = splitted_num[0]
    parte_decimal = splitted_num[-1]
    return f"R$ {parte_inteira},{parte_decimal}"
