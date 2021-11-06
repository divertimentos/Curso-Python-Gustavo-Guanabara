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


def moeda(num=0, moeda="R$"):
    return f"{moeda} {num:.2f}".replace(".", ",")


def resumo(num=0, aumento=0, diminuicao=0):
    resultado = f"""
Preço analisado: {moeda(num)}
Dobro do preço: {dobro(num, True)}
Metade do preço: {metade(num, True)}
{aumento}% de aumento: {aumentar(num, aumento, True)}
{diminuicao}% de redução: {diminuir(num, diminuicao, True)}
    """
    return resultado
