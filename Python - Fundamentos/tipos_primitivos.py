"""
    tipos_primitivos.py
    Autor: Iago Magalhães
    Descrição:
        - Mostrar exemplos de como declarar variaveis em Python
"""

# Tipo inteiro
idade = 23
dia = 9
mes = 5
ano = 2023

print(type(idade))
print(type(dia))
print(type(mes))
print(type(ano))

# Ponto Flutuante ou Decimal (float)
peso = 65
polegada = 25.4

print(type(peso))
print(type(polegada))

# Complexo (complex)
a = 5+2j
b = 20+6j

print(type(a))
print(type(b))
print(complex(2, 5))

# String (str)
nome = 'Iago'
sobrenome = 'Magalhães'

print(type(nome))
print(type(sobrenome))

# Boolean (bool)
verdade = True
falso = False

print(type(verdade))
print(type(falso))

# Listas (list)
lista = [1, 2, 3, 4.0, 5.0, 6.0, 'A', 'B', 'c', 'd', ['abc']]

print(type(lista))

# Tuplas (tuple)
tupla = (2, 2)

print(type(tupla))

# Dicionários (dict)
altura = {'Sarah': 1.65, 'Karol': 1.60, 'Isabela': 1.70}

print(type(altura))