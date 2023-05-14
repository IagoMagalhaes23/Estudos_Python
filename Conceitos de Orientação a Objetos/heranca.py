"""
    heranca.py
    Autor: Iago Magalhães
    Descrição:
        - entender o conceito de heranca através de exemplos
"""

#Criando classe pai
class Animal():
    def __init__(self, nome, cor):
        self.__nome = nome
        self.__cor = cor

    def comer(self):
        print(f"O {self.__nome} está comendo")

#Criando classe filho que herda da classse pai
class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

#Criando classe filho que herda da classse pai
class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

#Criando classe filho que herda da classse pai
class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

#Utilizando classes filhos
gato = Gato("Bichano", "Branco")
cachorro = Cachorro("Totó", "Preto")
coelho =Coelho("Pernalonga", "Cinza")

gato.comer()
cachorro.comer()
coelho.comer()

#Resultados esperados
# O Bichano está comendo
# O Totó está comendo
# O Pernalonga está comendo