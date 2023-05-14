"""
    classes.py
    Autor: Iago Magalhães
    Descrição:
        - entender o conceito de classes através de exemplos
"""

class Conta:
    def __init__(self, numero, titular, senha, saldo=0.0):
        self.numero = numero
        self.titular = titular
        self.senha = senha
        self.saldo = saldo
    
    def saque(self, senha, valor):
        if(self.senha == senha):
            if(self.saldo >= valor):
                self.saldo -= valor
                print("Saque em R$ ", valor)
            else:
                print("Saque inválido")
        else:
            print("Senha inválida")
    
    def deposito(self, senha, valor):
        if(self.senha == senha):
            if(valor > 0):
                self.saldo += valor
            else:
                print("Depósito inválido")
        else:
            print("Senha inválida")
    
    def exibirInfo(self):
        print("--------------------------")
        print(self.numero)
        print(self.titular)
        print(self.saldo)
        print("--------------------------")

c1 = Conta("0085", "Daniel", 1234, 100)
c1.saque(1234, 50)
c1.deposito(1234, 100)
c1.exibirInfo()

c2 = Conta("0095", "Rafael", 5678, 1000)