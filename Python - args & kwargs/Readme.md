# Python - args & kwargs

## Tópicos objetivos:
   - As variáveis mágicas *args e **kwargs são normalmente usadas na definições de uma função, e são usadas para passar um número desconhecido de argumentos para uma função.
   - Entender a diferença entre *args e **kwargs

## Estado da arte

### *args e **kwargs
*Args e **kwargs permitem que você passe um número não especificado de argumentos para uma função.

Dessa forma, ao escrever uma função, você não precisa definir quantos argumentos serão passados para sua função.

Observação importante: Escrever *args e **kwargs é apenas uma convenção: *args vem do inglês “arguments” (argumntos) e **kwargs vem do inglês “keyword arguments” (argumentos nomeados).

### Argumentos não nomeados *args
O *args é usado para receber uma lista de argumentos de comprimento variável sem a palavra-chave (keyword) na função.
- Exemplo 01:
    def função_com_argumentos_variaveis(arg, *args):
        print("Primeiro argumento:", arg)
        
        for agumento in args:
            print("Argumento de *args", argumento)

    função_com_argumentos_variaveis('primeiro_arg', 'arg2',     'arg3', 'arg3')

- Saída:
    Primeiro argumento: primeiro_arg
    Argumento de *args: arg2
    Argumento de *args: arg3
    Argumento de *args: arg3

Argumentos não nomeados (*args) vem sempre primeiro que os argumentos nomeados (**kwargs).

Veja a seguinte chamada de função:
    funcao_com_argumentos_variaveis(arg='arg', 'arg2', 'arg3', 'arg3') 
O seguinte erro será lançado:
    File "<stdin>", line 1
    SyntaxError: positional argument follows keyword argument

Uma função que soma os argumentos passados, independente do número de argumentos que seja passado, veja:
    def adicao(*args):
        resultado = 0
        
        for argumento in args:
            resultado += argumento

        return resultado

    print(adicao(1, 2))
    print(adição(1, 2, 4, 6))
    print(adição(1, 2, 4, 6, 8, 10))

- Saída:
    3
    31
    31

### Argumentos nomeados **kwargs
O **kwargs possibilita verificarmos os parâmetros nomeados da função, isto é, aqueles parâmetros que são passados com um nome!

Eles estarão disponíveis como um dicionário ({'chave': 'valor'}) dentro da função.

Vamos ao exemplo:
    def concatena (**kwargs):
        print(f'Valores recebidos: {kwargs}')
        resultado = ""

        for valor in kwargs.values():
            resultado += f'{valor} '
        return resultado

    print(concatena(a="Python", b="Academy",  c="Rules!"))
    print()
    print(concatena(a="Python", b="é", c="na", d="Python", e="Academy!"))

Veja a saída, perceba que recebemos um dict na variável kwargs:
    Valores recebidos: {'a': 'Python', 'b': 'Academy', 'c': 'Rules!'}
    Python Academy Rules! 

    Valores recebidos: {'a': 'Python', 'b': 'é', 'c': 'na', 'd': 'Python', 'e': 'Academy!'}
    Python é na Python Academy!

Para melhor entender vamos juntar tudo e printar o que vem em cada um dos tipos de parâmetros.

Veja o exemplo:
    def funcao(arg_1, arg_2, *args, arg_kw, **kwargs):
        print(f'Parâmetro 1: {arg_1}')
        print(f'Parâmetro 2: {arg_2}')
        print(f'*args: {args}')
        print(f'Argumento nomeado: {arg_kw}')
        print(f'**kwargs: {kwargs}')

    # Chamada da Função
    funcao(
        1,          # Parâmetro 1
        'a',        # Parâmetro 2
        'arg1',     # *args
        'arg2',     # *args
        2,          # *args
        arg_kw='KW',# arg_kw
        banana='B', # **kwargs
        bananas='A' # **kwargs
    )

A saída deste código será:
    Parâmetro 2: a
    *args: ('arg1', 'arg2', 2)
    Argumento nomeado: KW
    **kwargs: {'banana': 'B', 'bananas': 'A'}

## Referências
- https://pythonacademy.com.br/blog/args-e-kwargs-do-python
- https://realpython.com/python-kwargs-and-args/