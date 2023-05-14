"""
    abstracoes.py
    Autor: Iago Magalhães
    Descrição:
        - entender o conceito de abstracoes através de exemplos
"""

#Exemplo 01
from abc import ABC, abstractmethod 
  
class Polygon(ABC): 
  
    
    def noofsides(self): 
        pass
  
class Triangle(Polygon): 
  
    
    def noofsides(self): 
        print("I have 3 sides") 
  
class Pentagon(Polygon): 
  
    
    def noofsides(self): 
        print("I have 5 sides") 
  
class Hexagon(Polygon): 
  
    
    def noofsides(self): 
        print("I have 6 sides") 
  
class Quadrilateral(Polygon): 
  
    
    def noofsides(self): 
        print("I have 4 sides") 
R = Triangle() 
R.noofsides() 
  
K = Quadrilateral() 
K.noofsides() 
  
R = Pentagon() 
R.noofsides() 
  
K = Hexagon() 
K.noofsides()

#Resultado esperado
# Eu tenho 3 lados
# Eu tenho 4 lados
# Eu tenho 5 lados
# Eu tenho 6 lados

#Exemplo 02
from abc import ABC, abstractmethod 
class Animal(ABC): 
  
    def move(self): 
        pass
  
class Human(Animal): 
  
    def move(self): 
        print("I can walk and run") 
  
class Snake(Animal): 
  
    def move(self): 
        print("I can crawl") 
  
class Dog(Animal): 
  
    def move(self): 
        print("I can bark") 
  
class Lion(Animal): 
  
    def move(self): 
        print("I can roar") 
          
R = Human() 
R.move() 
  
K = Snake() 
K.move() 
  
R = Dog() 
R.move() 
  
K = Lion() 
K.move()

#Resultado esperado
# Eu posso andar e correr
# Eu posso rastejar
# Eu posso latir
# Eu posso rugir

#Exemplo 03
import abc 
  
class parent:        
    def geeks(self): 
        pass
  
class child(parent): 
    def geeks(self): 
        print("child class") 
print( issubclass(child, parent)) 
print( isinstance(child(), parent)) 

#Resultado esperado
# Verdade
# Verdade

#Exemplo 04
import abc 
from abc import ABC, abstractmethod 
  
class R(ABC): 
    def rk(self): 
        print("Abstract Base Class") 
  
class K(R): 
    def rk(self): 
        super().rk() 
        print("subclass ") 
r = K() 
r.rk()

#Resultado esperado
# Classe Base Abstrata
# subclasse

#Exemplo 05
import abc 
from abc import ABC, abstractmethod 
  
class parent(ABC): 
    @abc.abstractproperty 
    def geeks(self): 
        return "parent class"
class child(parent): 
       
    @property
    def geeks(self): 
        return "child class"
   
   
try: 
    r =parent() 
    print( r.geeks) 
except Exception as err: 
    print (err) 
   
r = child() 
print (r.geeks)

#Resultado esperado
# Não é possível instanciar a classe abstrata pai com métodos abstratos geeks
# classe infantil

#Exemplo 06
from abc import ABC,abstractmethod 
  
class Animal(ABC): 
    @abstractmethod
    def move(self): 
        pass
class Human(Animal): 
    def move(self): 
        print("I can walk and run") 
  
class Snake(Animal): 
    def move(self): 
        print("I can crawl") 
  
class Dog(Animal): 
    def move(self): 
        print("I can bark") 
  
class Lion(Animal): 
    def move(self): 
        print("I can roar") 
  
c=Animal()

#Resultado esperado
# Traceback (última chamada mais recente):
#   Arquivo "X", linha Y, em
#     c = Animal()
# TypeError: Não é possível instanciar a classe abstrata Animal com métodos abstratos move