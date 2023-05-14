"""
    listas.py
    Autor: Iago Magalhães
    Descrição:
        - Mostrar exemplos de como declarar listas em Python
"""

#Coleções
lst = [10, 'a', 'Supervisório', 5.6, True, [5,6], [[1,2],[4,5]]]

print(lst[2])       #valor da posição 2
print(lst[1:4])     #valor da posição 1 até 3 [4
print(lst[-2])      #valor da posição -2
print(lst[-2:])     #valor da penúltima posição até o final
print(lst[-2][1])   #valor da penúltima posição, índice 1
print(lst[6][1][1]) #valor da posição 6, índice 1 da linha, índice 1 da coluna

lst = [1, 'a', 5.5, False]
lst.append(10)      #acrescenta o elemento 10 no final da lista
print(lst)
lst.insert(1, True) #insere True na posição 1 da lista
print(lst)
lst.remove(5.5)     #remove o elemento 5.5
print(lst)
del lst[0]          #deleta a posição do índice 0
print(lst)