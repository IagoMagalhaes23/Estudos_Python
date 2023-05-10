# Python Fundamentos:

## Tópicos objetivos:
    - Python é uma linguagem de programação de alto nível, de uso geral, amplamente utilizada em aplicações web, desenvolvimento de software, ciência de dados e Machine Learning. Sua filosofia de projeto enfatiza a legibilidade do código com o uso de indentação significativa. Python é dinamicamente tipada e tem um garbage collector.
    - Conhecer os tipos primitivos
    - Declarar variáveis, considerando os diferentes tipos
    - Usar estruturas condicionais ('if', 'else')
    - Conhecer os operadores de comparação
    - Usar estruturas de repetição e laços ('while', 'for')
    - Usar funções, passando parâmetros e argumentos
    - Manipular métodos
    - Manipular arrays e listas
    - Obter dados de uma API
    - Criar construtores
    - Funções anônimas

## Estudo da arte
    Python é uma linguagem dinamicamente tipada, o que significa que não é necessário declarar o tipo de variável ou fazer casting (mudar o tipo de variável), pois o Interpretador se encarrega disso para nós!
    Os tipos de dados padrão do Python são:
        - Inteiro (int)
        - Ponto Flutuante ou Decimal (float)
        - Tipo Complexo (complex)
        - String (str)
        - Boolean (bool)
        - List (list)
        - Tuple
        - Dictionary (dic)

### Tipo Inteiro (int)
    O tipo inteiro é um tipo composto por caracteres numéricos (algarismos) inteiros.

    É um tipo usado para um número que pode ser escrito sem um componente decimal, podendo ter ou não sinal, isto é: ser positivo ou negativo.
### Ponto Flutuante ou Decimal (float)
    É um tipo composto por caracteres numéricos (algarismo) decimais.

    O famoso ponto flutuante é um tipo usado para números racionais (números que podem ser representados por uma fração) informalmente conhecido como “número quebrado”.
### Complexo (complex)
    Tipo de dado usado para representar números complexos (isso mesmo, aquilo que provavelmente estudou no terceiro ano do ensino médio).

    Esse tipo normalmente é usado em cálculos geométricos e científicos.

    Um tipo complexo contem duas partes: a parte real e a parte imaginária, sendo que a parte imaginária contem um j no sufixo.
### String (str)
    É um conjunto de caracteres dispostos numa determinada ordem, geralmente utilizada para representar palavras, frases ou textos.
### Boolean (bool)
    Tipo de dado lógico que pode assumir apenas dois valores: falso ou verdadeiro (False ou True em Python).
### Listas (list)
    Tipo de dado muito importante e que é muito utilizado no dia a dia do desenvolvedor Python!

    Listas agrupam um conjunto de elementos variados, podendo conter: inteiros, floats, strings, outras listas e outros tipos.
### Tuplas (tuple)
    Assim como Lista, Tupla é um tipo que agrupa um conjunto de elementos.

    Porém sua forma de definição é diferente: utilizamos parênteses e também separado por vírgula.

    A diferença para Lista é que Tuplas são imutáveis, ou seja, após sua definição, Tuplas não podem ser modificadas.
### Dicionários (dict)
    Dict é um tipo de dado muito flexível do Python.

    Eles são utilizados para agrupar elementos através da estrutura de chave e valor, onde a chave é o primeiro elemento seguido por dois pontos e pelo valor.

### Estruturas condicionais: if, else e elif
    Uma estrutura condicional é aquela que faz uma verificação em uma determinada expressão para identificar se ela atende à condição especificada.
### Operadores de comparação
    Os operadores são usados na construção de expressões, as quais contém um número variado de operandos. Por exemplo, na expressão a + b, temos o operador de aritmético + e operandos são as variáveis a e b.

    Na linguagem Python temos a seguinte separação entre os diferentes tipos de operadores:

    - Operadores aritméticos
    - Operadores de atribuição
    - Operadores de comparação
    - Operadores lógicos
    - Operadores de identidade
    - Operadores de associação
### Estruturas de repetição: while e for
    As estruturas de repetição são recursos das linguagens de programação responsáveis por executar um bloco de código repetidamente através de determinadas condições especificas.

    O Python contém dois tipos de estruturas de repetição: for e while.
### Funções
    Na programação, funções são blocos de código que realizam determinadas tarefas que normalmente precisam ser executadas diversas vezes dentro de uma aplicação. Quando surge essa necessidade, para que várias instruções não precisem ser repetidas, elas são agrupadas em uma função, à qual é dado um nome e que poderá ser chamada/executada em diferentes partes do programa.

### Obter dados de uma API
    API significa Application Programming Interface (Interface de Programação de Aplicação). No contexto de APIs, a palavra Aplicação refere-se a qualquer software com uma função distinta. A interface pode ser pensada como um contrato de serviço entre duas aplicações. Esse contrato define como as duas se comunicam usando solicitações e respostas. A documentação de suas respectivas APIs contém informações sobre como os desenvolvedores devem estruturar essas solicitações e respostas.
### Construtores
    Para declarar atributos na classe podemos utilizar um construtor, um método especial que inicializa o objeto e define a sua estrutura (seus atributos) durante o processo de instanciação. No Python o construtor é chamado __init__ e podemos utilizá-lo como ilustra o código a seguir.

    class Pessoa:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade
### Funções anônimas
    Funções lambda são uma ferramenta poderosa na programação Python, que permite a criação de funções anônimas, ou seja, sem necessidade de dar um nome para elas.

    Elas são úteis quando precisamos de uma função simples, que será utilizada apenas uma vez e não precisa ser reutilizada em outro lugar do código.

## Arquivos .py
### tipos_primitivos.py
Mostra exemplos de como declarar variaveis em Python.
### estruturas_condicionais.py
Mostra exemplos de como utilizar estruturas condicionais.
### operadores_comparacao.py
Mostra exemplos de como utilizar operadores de comparação.
### estruturas_repeticao.py
Mostra exemplos de como utilizar estruturas de repetição.
### funcoes.py
Mostra exemplos de como declarar e utilizar funções.
### manipular_metodos.py
Mostra exemplos de como manipular métodos.
### manipular_array_listas.py
Mostra exemplos de como manipular arrays e listas.
### obter_dados_api.py
Mostra exemplos de como obter dados de uma API.
### construtores.py
Mostra exemplos de como utilizar construtores.
### funcoes_anonimas.py
Mostra exemplos de como utilizar funções anônimas.

## Referências
- https://pythonacademy.com.br/blog/tipos-de-variaveis-no-python
- https://blog.betrybe.com/python/if-else/
- https://www.devmedia.com.br/operadores-no-python/40693
- https://pythonacademy.com.br/blog/estruturas-de-repeticao
- https://www.devmedia.com.br/funcoes-em-python/37340
- https://terminalroot.com.br/2021/11/aprenda-25-exemplos-de-metodos-para-strings-em-python.html
- https://algoritmosempython.com.br/cursos/programacao-python/listas/
- https://aws.amazon.com/pt/what-is/api/#:~:text=API%20significa%20Application%20Programming%20Interface,de%20servi%C3%A7o%20entre%20duas%20aplica%C3%A7%C3%B5es.
- https://jacksongomesbr.gitbooks.io/programacao-orientada-a-objetos-com-python/content/objetos-em-python.html
- https://pythonacademy.com.br/blog/funcoes-lambda-no-python#:~:text=Fun%C3%A7%C3%B5es%20lambda%20s%C3%A3o%20uma%20ferramenta,em%20outro%20lugar%20do%20c%C3%B3digo.
- https://www.treinaweb.com.br/blog/consumindo-apis-com-python-parte-1