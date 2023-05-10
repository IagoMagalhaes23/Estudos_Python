"""
    funcoes_anonimas.py
    Autor: Iago Magalhães
    Descrição:
        - Mostrar exemplos de como utilizar funções anônimas em Python
"""

#Sua sintaxe básica é a seguinte:
#lambda {argumentos}: {expressão}

soma = lambda x, y: x + y
print(soma(2, 3))

#Podemos armazenar a função lambda em uma variável, como no exemplo acima, ou chamá-la diretamente:
print((lambda x, y: x + y)(2, 3))

#Veja o exemplo abaixo, onde usamos a função map para aplicar uma função lambda que eleva cada elemento de uma lista ao quadrado:
lista = [1, 2, 3, 4]

print(list(map(lambda x: x ** 2, lista)))

#No exemplo abaixo,usamos a função filter para retornar apenas os números pares de uma lista:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(filter(lambda x: x % 2 == 0, lista)))

#Por fim, veja o exemplo a seguir, onde usamos a função reduce para somar todos os elementos de uma lista:
from functools import reduce

lista = [1, 2, 3, 4, 5]

print(reduce(lambda x, y: x + y, lista))