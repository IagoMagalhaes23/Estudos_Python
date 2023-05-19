# Python - Tipagem estática

## Tópicos objetivos:
   - Python é uma linguagem dinamicamente tipada, ou seja, não há necessidade de pensar em tipos de dados. Linguagens estaticamente tipadas (tais como C ou Java) realizam verificações de tipo durante a compilação. Pode parecer mais seguro, pois você pode dizer imediatamente o tipo de parâmetro de cada função.
   - Conhecer type hinting

## Estado da arte

### Tipagem estática e dinâmica
Em suma, em uma linguagem de tipagem estática, o tipo de uma variável é determinado em tempo de compilação e não pode ser alterado em tempo de execução. Isso significa que você deve especificar o tipo de dado de uma variável ao declará-la e não pode atribuir um valor de tipo diferente a essa variável. As linguagens de tipagem estática geralmente têm regras mais rígidas para verificação de tipo, o que pode torná-las mais difíceis de aprender e usar, mas também podem fornecer alguns benefícios em termos de clareza de código e verificação de erros.

Contudo, em uma linguagem de tipagem dinâmica, o tipo de uma variável é determinado em tempo de execução, não em tempo de compilação. Isso significa que você não precisa informar o tipo de uma variável ao declará-la, e a mesma pode conter valores de tipos diferentes em momentos diferentes. Linguagens de tipagem dinâmica geralmente são mais fáceis de aprender e usar, porque são mais flexíveis e permitem que você escreva código rapidamente. No entanto, elas também podem ser menos previsíveis e podem levar a erros de tempo de execução se você não for cuidadoso.

### O que são Type Hints?
Primeiramente, Type Hints são um recurso que permite especificar o tipo de dados de uma variável em seu código. Type Hints não são executadas em tempo de execução, mas podem ser usadas por ferramentas como IDEs e type checkers para fornecer informações adicionais sobre o código. Por exemplo, se você tiver uma função que aceita um número inteiro como argumento, poderá usar um Type Hint para indicar que o argumento deve ser um int.

Contudo, é importante notar que Type Hints não tornam o Python uma linguagem estaticamente tipada. Além disso, Types Hints são completamente opcionais e não são necessários para escrever código Python. Você pode usá-los se quiser, mas eles não alteram a natureza dinâmica da linguagem.

### PEPs relacionadas ao Type Hints
- PEP 484, “Type Hints”, introduziu a sintaxe para especificar Type Hints em Python e definiu a semântica de como elas devem ser interpretadas por ferramentas como IDEs e verificadores de tipo. Esta PEP também introduziu o módulo typing, que fornece uma biblioteca padrão de definições de Type Hints.
- PEP 526, “Syntax for Variable Annotations”, estendeu a sintaxe de Type Hints para permitir que sejam usadas em variáveis, bem como em argumentos de função e valores de retorno. Esta PEP também introduziu o caractere : como um atalho para especificar o tipo de uma variável.
- PEP 589, “TypedDict: Type Hints for Dictionaries with a Fixed Set of Keys”, introduziu o tipo TypedDict, que permite que você especifique um tipo de dados para um dicionário que tenha um conjunto fixo de chaves. Isso permite que você especifique um tipo de dados mais específico para um dicionário, em vez de usar o tipo genérico Dict.
- PEP 563, “Postponed Evaluation of Annotations”, introduziu suporte para avaliação adiada de Type Hints. Isso permite que os Type Hints se refiram a nomes que ainda não foram definidos no momento em que o Type Hint é avaliado, o que pode ser útil em determinados casos.

### Por que usar Type Hints?
Certamente existem várias razões pelas quais você pode querer usar Type Hints em seu código Python. Aqui estão algumas delas:

Type Hints podem ser usadas por ferramentas como IDEs e verificadores de tipo para fornecer informações adicionais sobre o código. Por exemplo, uma IDE pode usar Type Hints para fornecer sugestões de código e verificar se você está usando o tipo correto de dados em uma variável.
Type Hints podem ser usadas para documentar o código. Isso pode ser útil se você estiver trabalhando em um projeto com várias pessoas, pois permite que você especifique o tipo de dados que uma variável deve conter.
Type Hints podem ser usadas para verificar se o código está usando o tipo correto de dados em uma variável. Isso pode ser útil para encontrar erros de digitação ou erros de lógica que podem ser difíceis de encontrar em tempo de execução.
Type Hints podem ser usadas para otimizar o código em tempo de execução. Por exemplo, se você usar Type Hints para especificar que uma variável contém um número inteiro, o interpretador Python pode usar uma implementação mais rápida de operações matemáticas em vez de uma implementação genérica que funciona com qualquer tipo de dados.
No geral, o uso de Type Hints pode fornecer vários benefícios, mas não substitui testes e depurações cuidadosos. Elas são apenas uma ferramenta em seu kit de ferramentas para escrever código Python de alta qualidade.

### Como usar Type Hints?
Agora que você sabe o que são Type Hints e por que elas são úteis, vamos ver como usá-las em seu código Python. A sintaxe de Type Hints é muito simples e consiste em dois operadores:

: é usado para especificar o tipo de dados de uma variável.
-> é usado para especificar o tipo de dados de um valor de retorno.
Por exemplo, aqui está uma função que aceita um argumento nome e retorna uma string:
    def saudacao(nome: str) -> str:
        return f"Olá {nome}"

### Tipos básicos
Para especificar o tipo de uma variável ou valor de retorno, você pode usar os tipos básicos do Python (por exemplo, str, int, bool, etc.).
    string: str = "Olá"
    inteiro: int = 123
    booleano: bool = True
    ponto_flutuante: float = 1.23
    string_bytes: bytes = b"Olá"

### Tipos de coleções
Também é possível utilizar tipos referentes a coleções.
    lista: list = [1, 2, 3]
    tupla: tuple = (1, 2, 3)
    conjunto: set = {1, 2, 3}
    dicionario: dict = {"a": 1, "b": 2, "c": 3}

Outro exemplo é:
    lista_inteiros: list[int] = [1, 2, 3]
    tupla_inteiros: tuple[int, int, int] = (1, 2, 3)
    conjunto_inteiros: set[int] = {1, 2, 3}
    dicionario_strings_inteiros: dict[str, int] = {"a": 1, "b": 2, "c": 3}

No entanto, é importante notar que essa sintaxe só funciona a partir do Python 3.9. Se você estiver usando uma versão anterior do Python, você pode usar a sintaxe typing.List, typing.Tuple, typing.Set e typing.Dict para especificar o tipo de dados que cada elemento da coleção deve conter.

### Tipagem de classes
Também é possível utilizar classes para especificar o tipo de dados de uma variável.

    class Pessoa:
        def __init__(self, nome: str, idade: int):
            self.nome = nome
            self.idade = idade

    pessoa: Pessoa = Pessoa("João", 20)

### Tipos especiais
Existem alguns tipos especiais que podem ser usados para especificar o tipo de dados de uma variável.

- Any: pode conter qualquer tipo de dados;
- Union: pode conter um dos tipos de dados especificados;
- Optional: pode conter um dos tipos de dados especificados ou None;
- Literal: pode conter um dos valores literais especificados;
- Final: pode especificar uma constante.
- Iterable: pode conter qualquer tipo de dados que possa ser iterado, ou seja, qualquer tipo de dados que possa ser usado em um loop for.
- Sequence: pode conter qualquer tipo de dados que possa ser indexado, ou seja, qualquer tipo que suporte à notação de colchetes;
- Mapping: pode conter qualquer tipo de dados que possa ser mapeado;
- MutableMapping: pode conter qualquer tipo de dados que possa ser mapeado e mutável;
- Callable: pode conter qualquer tipo de dados que possa ser chamado.

    from typing import (
        Any,
        Union,
        Optional,
        Literal,
        Final,
        Iterable,
        Sequence,
        Mapping,
        MutableMapping,
        Callable
    )

    variavel_any: Any = 123
    variavel_union: Union[int, str] = 123
    variavel_optional: Optional[int] = 123
    variavel_literal: Literal[1, 2, 3] = 1
    variavel_final: Final = 123
    variavel_iterable: Iterable[int] = [1, 2, 3]
    variavel_sequence: Sequence[int] = [1, 2, 3]
    variavel_mapping: Mapping[str, int] = {"a": 1, "b": 2, "c": 3}
    variavel_mutable_mapping: MutableMapping[str, int] = {"a": 1, "b": 2, "c": 3}
    variavel_callable: Callable[[int, int], int] = lambda x, y: x + y

Para podermos entender melhor o que cada um desses tipos especiais faz, vamos criar uma função que recebe uma lista de números e retorna a soma de todos os números da lista.

    from typing import Iterable

    def soma_numeros(numeros: Iterable[int]) -> int:
        soma = 0
        for numero in numeros:
            soma += numero
        return soma

Para especificar que a função recebe uma lista de números, nós utilizamos o tipo Iterable[int]. Com a finalidade de especificar que a função retorna um número, nós utilizamos o tipo int. Aqui o tipo Iterable[int] foi utilizado porque a função pode receber qualquer tipo de dados que possa ser iterado, ou seja, qualquer tipo de dados que possa ser usado em um loop for. Por exemplo, a função pode receber uma lista de números, uma tupla de números, um conjunto de números, um dicionário de números, etc.

Agora vamos testar a função soma_numeros com alguns tipos de dados diferentes.

    print(soma_numeros([1, 2, 3]))
    print(soma_numeros((1, 2, 3)))
    print(soma_numeros({1, 2, 3}))
    print(soma_numeros({"a": 1, "b": 2, "c": 3}))

## Referências
- https://www.treinaweb.com.br/blog/tipagem-no-python-com-type-hints
- https://docs.python.org/3/library/typing.html
- https://realpython.com/lessons/type-hinting/