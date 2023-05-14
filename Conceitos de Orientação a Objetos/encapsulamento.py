"""
    encapsulamento.py
    Autor: Iago Magalhães
    Descrição:
        - entender o conceito de encapsulamento através de exemplos
"""

#Exemplo 01
class Funcionario1:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.horas_trabalhadas = 0
        self.salario = 0

    def registra_hora_trabalhada(self):
        self.horas_trabalhadas += 1

    def calcula_salario(self):
        self.salario = self.horas_trabalhadas * self.valor_hora_trabalhada

pedro = Funcionario1('Pedro', 'Gerente de Vendas', 50)
pedro.__salario = 100000
print(pedro.__salario)

#Resultado esperado
# 100000

#Exemplo 02
class Funcionario2:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__salario = 0
        self.__horas_trabalhadas = 0

    @property
    def salario(self): 
        return self.__salario

    @salario.setter
    def salario(self, novo_salario): 
        raise ValueError("Impossivel alterar salario diretamente. Use a funcao calcula_salario().")

    def registra_hora_trabalhada(self):
        self.__horas_trabalhadas += 1

    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada

pedro = Funcionario2('Pedro', 'Gerente de Vendas', 50)
pedro.salario = 100000

#Resultado esperado
# Traceback (most recent call last):
#   File "teste.py", line 26, in <module>
#     f.salario = 1000
#   File "teste.py", line 16, in salario
#     raise ValueError("Impossivel alterar salario diretamente. Use a funcao calcula_salario().")
# ValueError: Impossivel alterar salario diretamente. Use a funcao calcula_salario().

#Isso mesmo, um erro, porque não podemos acessar e alterar o salario, devido ao uso do decorador @property