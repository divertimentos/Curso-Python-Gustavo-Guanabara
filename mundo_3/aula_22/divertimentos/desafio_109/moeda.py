def dobro(num=0, is_formatted=False):
    resultado = num * 2
    return moeda(resultado) if is_formatted else resultado


def metade(num=0, is_formatted=False):
    resultado = num / 2
    return moeda(resultado) if is_formatted else resultado


def aumentar(num=0, taxa=0, is_formatted=False):
    resultado = num + (taxa * num / 100)
    return moeda(resultado) if is_formatted else resultado


def diminuir(num=0, taxa=0, is_formatted=False):
    resultado = num - (taxa * num / 100)
    return moeda(resultado) if is_formatted else resultado


def moeda(num, moeda="R$"):
    return f"{moeda} {num:.2f}".replace(".", ",")
