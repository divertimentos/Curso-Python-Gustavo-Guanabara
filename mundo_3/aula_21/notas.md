# Aula 21: Funções (Parte 2)

## Interactive Help

`help(print)` ou `print(input.__doc__)`

## Docstrings

São strings de documentação das funcionalidades de alguma função no Python.

```python
def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return sem retorno
    """

    c = i
    while c <= f:
        print(f"{c}", end=", ")
        c+= p
    print("FIM!")

    print(help(contador))

```

## Parâmetros opcionais

```python
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f"A soma vale: {s}.")

somar(8, 4)
somar()
somar(b=4, c=2)
```

## Escopo de variáveis

```python
# Local:
def teste():
  x = 8
  print(f"Na função teste, n vale {n}")
  print(f"Na função teste, x vale {x}")

# Programa principal (global):
n = 2
print(f"No programa principal, n vale {n}")
print(f"No programa principal, x vale {x}")  # <-- Isso quebra o código
```

O código quebra porque x não é uma variável global; ela é interna (local) à função `teste()`.

Uma inovação do Python frente a outras linguagens de programação é a possibilidade de existirem duas variáveis com o mesmo nome -- uma global e outra local -- habitando o mesmo código e recebendo valores de forma independente.

```python
def funcao():
    variavel = "dentro"
    print(f"Variável dentro recebe: {variavel}")

variavel = "fora"
funcao()
print(f"Variável fora recebe: {variavel}")
```

Para reverter esse recurso, ou seja, usar o valor global de uma variável tanto fora quando dentro de uma função, utilize `global nome_da_variavel` abaixo da definição da função:

```python
def funcao(parametro):
    global a
    a = 8
    print(f"'a' vale {a}")
a = 5
funcao(a)
print(f"'a' fora vale {a}")
```

Neste código, a função irá printar `8`.

## Retorno de valores

```python
def somar(a=3, b=0, c=0):
    s = a + b + c
    return s

# print(somar(3, 2, 5))
# print(somar(2, 2))
# print(somar(6))

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f"Os resultados foram {r1}, {r2} e {r3}.")
```
