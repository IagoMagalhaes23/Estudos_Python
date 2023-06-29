# Python - Multiprocessamento

## Tópicos de interesse:
   - Em Python, o módulo de multiprocessamento inclui uma API muito simples e intuitiva para dividir o trabalho entre vários processos.
   - Executar processos em paralelo
   - Conhecer a classe Pool

## Concorrência e Paralelismo
É comum achar que concorrência e paralelismo são a mesma coisa, mas não. Rob Pike , um dos criadores da linguagem Go , explicou em uma apresentação:

    Concorrência é sobre lidar com várias coisas ao mesmo tempo e paralelismo é sobre fazer várias coisas ao mesmo tempo.

Mas vamos a uma definição mais formal:

    **Concorrência** : "É a capacidade de se executar duas ou mais tarefas em um mesmo período de tempo"

    **Paralelismo** : "Paralelismo é sobre a execução paralela de tarefas, ou seja, mais de uma por vez de formal simultânea"

**Contexto**
Contexto é usado uma tarefa pode ser interrompida e em algum momento voltar a ser executada exatamente onde parou. Porém, existe um custo alto então quanto menor o contexto menor é a latência.

**Thread**
Em sistemas operacionais tradicionais, cada processo tem um espaço de endereçamento e um único thread (fluxo) de controle. As threads são utilizadas para que múltiplas execuções tenham permitidom no mesmo ambiente do processo com um grande grau de independência uma da outra.

Como cada thread pode ter acesso a qualquer endereço de memória dentro do espaço de endereçamento do processo, uma thread pode ler, escrever até ou mesmo apagar completamente a pilha de outra thread.

## Módulo de multiprocessamento do Python
Apresentando o módulo multiprocessingdo Python e como podemos usá-lo para enviar vários processos que podem ser executados independentemente um do outro, a fim de fazer o melhor uso dos nossos núcleos de CPU.

O módulo de multiprocessamento na Biblioteca Padrão do Python possui muitos recursos poderosos. Se você quiser ler sobre todos os detalhes e ir mais a fundo, recomendo o uso de documentos oficiais como ponto de entrada.

Nas seções a seguir, desejo fornecer uma breve visão geral para mostrar como o módulo de multiprocessamento poderá ser usado para programação paralelamente.

O multiprocessamento oferece vários recursos hoje eu quero focar na Classe Pool que é mais conveniente para tarefas simples de processamento paralelo.

Existem quatro métodos que são particularmente interessantes:

- Pool.apply
- Pool.map
- Pool.apply_async
- Pool.map_async

Os métodos Pool.apply e Pool.map são basicamente equivalentes às funções apply e map nativas do Python. Antes de chegarmos às variantes async dos métodos Pool, vamos dar uma sensação em um exemplo simples usando Pool.apply e Pool.map. Aqui definiremos o número de processos como 4, o que significa que a classe Pool permitirá apenas 4 processos em execução ao mesmo tempo.

```
from random import randint
from time import sleep, time
from multiprocessing.pool import ThreadPool

def print_names(name):
    sleep(randint(1, 3))
    print('Meu nome é: {}'.format(name))

runtime = []
threads = []
names = ['Adson', 'Gabriel', 'Siqueira', 'Ronaldo', 'Gleilson',
         'Emerson', 'Joselito', 'Piloto', 'Kleber', 'Mauricio']

pool = ThreadPool(processes=4)
start = time()

for name in names:
    async_result = pool.apply(print_names, (name,))
    threads.append(async_result)

end = time()
print('tempo de execução da tradução: {}'.format(end - start))
```

**tempo de execução da tradução: 21,03 segundos**

```
from random import randint
from time import sleep, time
from multiprocessing.pool import ThreadPool


def print_names(name):
    sleep(randint(1, 3))
    print('Meu nome é: {}'.format(name))


runtime = []
threads = []
names = ['Adson', 'Gabriel', 'Siqueira', 'Ronaldo', 'Gleilson',
         'Emerson', 'Joselito', 'Piloto', 'Kleber', 'Mauricio']

pool = ThreadPool(processes=4)
start = time()

for name in names:
    async_result = pool.map(print_names, (name,))
    threads.append(async_result)

end = time()
print('tempo de execução da tradução: {}'.format(end - start))
```

**tempo de execução da tradução: 24,03 segundos**

O Pool.map e Pool.apply bloqueará o programa principal que todos os processos sejam concluídos até, o que é bastante útil se queremos obter resultados ordenados.

Por outro lado, as variantes assíncronas enviarão todos os processos de uma só vez e recuperarão os resultados assim que terminarem. Outra diferença que é bastante importante é que precisamos usar o método get() após uma chamada de apply_async() para obter os valores dos processos concluídos.

```
from random import randint
from time import sleep, time
from multiprocessing.pool import ThreadPool


def print_names(name):
    sleep(randint(1, 3))
    print('Meu nome é: {}'.format(name))


runtime = []
threads = []
names = ['Adson', 'Gabriel', 'Siqueira', 'Ronaldo', 'Gleilson',
         'Emerson', 'Joselito', 'Piloto', 'Kleber', 'Mauricio']

pool = ThreadPool(processes=4)
start = time()

for name in names:
    async_result = pool.map_async(print_names, (name,))
    threads.append(async_result)

letters_list = [result.get() for result in threads]

end = time()
print('tempo de execução da tradução: {}'.format(end - start))
```

**tempo de execução da tradução: 6,00 segundos**

```
from random import randint
from time import sleep, time
from multiprocessing.pool import ThreadPool


def print_names(name):
    sleep(randint(1, 3))
    print('Meu nome é: {}'.format(name))


runtime = []
threads = []
names = ['Adson', 'Gabriel', 'Siqueira', 'Ronaldo', 'Gleilson',
         'Emerson', 'Joselito', 'Piloto', 'Kleber', 'Mauricio']

pool = ThreadPool(processes=4)
start = time()

for name in names:
    async_result = pool.apply_async(print_names, (name,))
    threads.append(async_result)

letters_list = [result.get() for result in threads]

end = time()
print('tempo de execução da tradução: {}'.format(end - start))
```

**tempo de execução da tradução: 6,01 segundos**

## Referências
- https://medium.com/@adson.develop/uma-pequena-introdu%C3%A7%C3%A3o-a-programa%C3%A7%C3%A3o-paralela-e-multiprocessamento-com-python-232bbf72a8f7