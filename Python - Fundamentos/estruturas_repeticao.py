"""
    estruturas_repeticao.py
    Autor: Iago Magalhães
    Descrição:
        - Mostrar exemplos de como utilizar estruturas de repetição em Python
"""

#For
for i in [0, 1, 2, 'string', [6, 7]]:
    print(i)

for i in range(3):
    print(i)

for i in range(1,3):
    print(i)

#While
i = 1
while i < 6:
    print(i)
    i += 1

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i não é menor que 6")