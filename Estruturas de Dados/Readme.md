# Estruturas de dados

## Tópicos objetivos:
   - No contexto dos computadores, uma estrutura de dados é uma forma específica de armazenar e organizar os dados na memória do computador para que esses dados possam ser facilmente recuperados e utilizados de forma eficiente quando necessário posteriormente.
   - Conhecer as principais estruturas de dados
   - Implementar as principais estruturas de dados

## Estudo da arte

### Introdução a Estrutura de dados
No Python, podemos utilizar diversos tipos de estruturas de dados. Estas estruturas resolvem um tipo de problema e podem ser úteis em diversas situações. As principais estruturas são as Listas, Sets, Dicionários e Tuplas.

### Listas
Uma lista é a estrutura de dados mais básica do Python e armazena os dados em sequência, onde cada elemento possui sua posição na lista, denominada de índice. O primeiro elemento é sempre o índice zero e a cada elemento inserido na lista esse valor é incrementado.

No Python, uma lista pode armazenar qualquer tipo de dado primitivo (string, inteiro, float, etc).

### Tuplas
Uma tupla é uma estrutura bastante similar a uma lista, com apenas uma diferença: os elementos inseridos em uma tupla não podem ser alterados, diferente de uma lista onde podem ser alterados livremente. Sendo assim, em um primeiro momento, podemos pensar em uma tupla como uma lista que não pode ser alterada, mas não é bem assim…

É certo que as tuplas possuem diversas características das listas, porém os usos são distintos. As listas são destinadas a serem sequências homogêneas, enquanto que as Tuplas são estruturas de dados heterogêneas.

Sendo assim, apesar de bastante similares, a tupla é utilizada para armazenar dados de tipos diferentes, enquanto que a lista é para dados do mesmo tipo.

### Tuplas vs Listas
As tuplas possuem algumas vantagens com relação às listas, que são:
- Como as tuplas são imutáveis, a iteração sobre elas é mais rápida e, consequentemente, possuem um ganho de desempenho com relação às listas;
- Tuplas podem ser utilizadas como chave para um dicionário, já que seus elementos são imutáveis. Já com a lista, isso não é possível;
- Se for necessário armazenar dados que não serão alterados, utilize uma tupla. Isso garantirá que esses sejam protegidos de alterações posteriores.

### Sets
No Python, os sets são uma coleção de itens desordenada, parcialmente imutável e que não podem conter elementos duplicados. Por ser parcialmente imutável, os sets possuem permissão de adição e remoção de elementos.

Além disso, os sets são utilizados, normalmente, com operações matemáticas de união, interseção e diferença simétrica.

### Dicionários
No Python, os dicionários são coleções de itens desordenados com uma diferença bem grande quando comparados às outras coleções (lists, sets, tuples, etc): um elemento dentro de um dicionário possui uma chave atrelada a ele, uma espécie de identificador. Sendo assim, é muito utilizado quando queremos armazenar dados de forma organizada e que possuem identificação única (como acontece em bancos de dados).

## Arquivos .py
### listas.py
Mostra exemplos de como declarar listas em Python.

### tuplas.py
Mostra exemplos de como declarar tuplas em Python.

### sets.py
Mostra exemplos de como declarar sets em Python.

### dicionarios.py
Mostra exemplos de como declarar dicionários em Python.

## Referências
- https://www.treinaweb.com.br/blog/principais-estruturas-de-dados-no-python
- https://www.treinaweb.com.br/blog/manipulando-sets-no-python/