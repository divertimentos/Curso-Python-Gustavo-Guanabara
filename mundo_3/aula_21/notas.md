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
```

**Obs.: parei em 20min**