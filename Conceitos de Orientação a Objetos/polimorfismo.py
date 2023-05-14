"""
    polimorfismo.py
    Autor: Iago Magalhães
    Descrição:
        - entender o conceito de polimorfismo através de exemplos
"""

#Exemplo 01
class Super:
 def hello(self):
  print("Olá, sou a superclasse!")

teste = Super()
teste.hello()

#Resultado esperado
#Olá, sou a superclasse!

#Exemplo 02
class Super:
 def hello(self):
  print("Olá, sou a superclasse!")
  
class Sub (Super):
 def hello(self):
  print("Olá, sou a subclasse!")

teste = Sub()
teste.hello()

#Resultado esperado
#Olá, sou a subclasse!

#Exemplo 03
class Super:
 def hello(self):
  print("Olá, sou a superclasse!")
  
class Sub (Super):
 def hello(self):
  print("Olá, sou a subclasse!")

class Subsub (Sub):
 def hello(self):
  print("Olá, sou a subsubclasse!")

teste = Subsub()
teste.hello()

#Resultado esperado
#Olá, sou a subsubclasse!