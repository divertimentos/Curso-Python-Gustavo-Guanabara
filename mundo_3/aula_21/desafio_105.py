"""
Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

quantidade de notas
a maior nota
a menor nota
a média da turma
a situação (opcional)

Adicione tambeem as docstrings da função
"""


def notas(*args, situacao=False):
    """Funcão para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param situacao: valor opcional, indicando se deve ou não adicionar a situação
    :return dicionário com várias informações sobre a situação da turma.
    """
    infos = dict()
    maior = menor = soma = media = 0
    infos["total"] = len(args)  # total

    for nota in args:  # maior
        if nota == 0:
            maior = nota
        if nota > maior:
            maior = nota
    infos["maior"] = maior

    for nota in args:  # menor
        menor = nota
        if nota < menor:
            menor = nota
    infos["menor"] = menor

    for nota in args:
        soma += nota
    infos["media"] = soma / infos["total"]

    if situacao:
        if infos["media"] < 6:
            infos["situacao"] = "RUIM"
        elif infos["media"] <= 7:
            infos["situacao"] = "BOM"
        elif infos["media"] >= 9:
            infos["situacao"] = "ÓTIMO"
    else:
        pass
    return infos


# Programa principal:
resp = notas(5.5, 2.5, 1.5, situacao=True)
print(resp)
