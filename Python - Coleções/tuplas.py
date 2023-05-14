"""
    tuplas.py
    Autor: Iago Magalhães
    Descrição:
        - Mostrar exemplos de como declarar tuplas em Python
"""

#Tupla
tupla = ("Aragão", 10, 2.5, 1/4)
print(tupla)
print(tupla[2])
print(tupla[:3])
print(tupla[2:4])
print(tupla[1:])
listaTupla = list(tupla)
listaTupla[0] = "Pereira"
print("Atualiza tupla:", listaTupla)