"""
    metodos.py
    Autor: Iago Magalhães
    Descrição:
        - entender o conceito de metodos através de exemplos
"""

class Calculadora:
    #Declarando método soma
    def soma(self, a, b):
        return a + b
    #Declarando método subtrai
    def subtrai(self, a, b):
        return a - b
    #Declarando método multiplica
    def multiplica(self, a, b):
        return a * b
    #Declarando método divide
    def divide(self, a, b):
        return a / b

#Usando metodos
#Declarando objeto da classe calculadora
c = Calculadora()
#Utilizando o método soma
print(c.soma(3,7))