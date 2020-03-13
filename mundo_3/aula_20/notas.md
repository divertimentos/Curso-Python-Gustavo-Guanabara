# Aula 20: Funções (Parte 1)

Funções são também conhecidas como métodos ou subrotinas.

# Conceitos introdutórios

* As funções estão atreladas ao conceito de rotina
* O print(), o len(), o input(), o int(), o float() etc. são funções *built-in* do Python
* As funções são criadas quando o programador precisa executar rapidamente uma ação que ele usa várias vezes, como, no exemplo do Guanabara, desenhar linhas na tela para enfeitar os prints dos exercícios.
  * Para isso, ele pode criar uma função chamada `mostra_linha()`
* Funções são diferentes de laços, pois, embora ambos aconteçam repetidamente no código, as funções diferem dos laços por aparecerem de forma espaçada, sem um padrão definido, ao longo do código.

* Para mostrar uma linha, basta criar uma função usando a seguinte sintaxe:

```python
def mostra_linha():
  print('--------------------------------')
	
```

* Outro detalhe é que, para que a função seja executada, ela precisa ser chamada:

  ```python
  def lin():
    print('-' * 30)
  
  lin() # <----------------- Chamamento da função
  # Programa principal
  print("Curso em Vídeo")
  lin()
  print("Aprenda Python")
  lin()
  print("Gustavo Guanabara")
  ```

# Parâmetros

Observando os padrões de repetição no código, podemos escrever funções nas quais as informações que variam são usadas como parâmetros, enquanto todo o restante é repetido pela função. Exemplo:

```python
# Código sem função

print("-" * 30)
print("Sistema de alunos")
print("-" * 30)

print("-" * 30)
print("Cadastro de funcionários")
print("-" * 30)

print("-" * 30)
print("Erro do sistema")
print("-" * 30)

# Código com função e parâmetro:

def escreve_mensagem(mensagem):
    print("-" * 30)
    print(mensagem)
    print("-" * 30)

escreve_mensagem("Sistema de Alunos")
escreve_mensagem("Cadastro de Funcionários")
escreve_mensagem("Erro do Sistema")
```

Outro exemplo, agora com números:

```python
# somas sem função:
a = 5
b = 4
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)

# somas com função:
def soma(a, b):
    s = a + b
    print(s)

soma(4, 5)
soma(8, 9)
soma(2, 1)
```

Você pode também definir em qual ordem os parâmetros passados serão usados dentro da função. Exemplo:

```python
def subtracao(a, b):
    print(f"A = {a} e B = {b}")
    s = a-b
    print(f"A subtração A-B = {s}")

subtracao(a=10, b=5)  # resp.: 5
subtracao(b=10, a=5)  # resp.: -5
```

# Empacotamento/Desempacotamento de parâmetros

Quando uma função é criada para receber dois parâmetros, mas você passa mais de dois, o Python briga com você. Por exemplo, se, na função `soma()` você passar `soma(4, 5, 1)`, você obterá um erro:

```python
In [9]: soma(4, 5, 1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-9-d358a8272d35> in <module>
----> 1 soma(4, 5, 1)

TypeError: soma() takes 2 positional arguments but 3 were given
```

Para criar uma função que desempacota parâmetros que o usuário imputa, basta usar um asterisco ("\*") antes do parâmetro. Esse parâmetro especial é chamado também de  `*arg`:

```python
def contador(*num):
	print(f"Recebi os valores {num} e eles são {len(num)}")

  
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
```

# Passando uma lista como parâmetro de uma função

```python
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
```



