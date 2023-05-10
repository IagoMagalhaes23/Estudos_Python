"""
    funcoes.py
    Autor: Iago Magalhães
    Descrição:
        - Mostrar exemplos de como utilizar funções em Python
"""


#Funções
print("Digite primeiro nome:")
nome = input()
print("Olá, " + nome)

nome = input("Digite nome e sobrenome:\n")
print("Olá, " + nome)

valor = int(input("Digite um número:\n"))
x = valor + 10
print("Resultado:", x)

#Definindo uma função
def imprimeElemLista(lista):
    for i in lista:
        print(i)

listaNum = [0, 3, 4, 5]
imprimeElemLista(listaNum)
listaStr = ["String1", "String2"]
imprimeElemLista(listaStr)

def imprimeChaveValor(dicionario):
    for chave, valor in dicionario.items():
        print(chave, valor, sep=": ")

parametrosMaq = {
    "Temp. máxima": 100.0,
    "Temp. min": 90.0,
    "Quat. aquecedores": 2,
    "Funcionamento": False,
    "Equipamento": "caldeira"
}

imprimeChaveValor(parametrosMaq)