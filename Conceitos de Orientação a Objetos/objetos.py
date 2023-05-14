"""
    objetos.py
    Autor: Iago Magalhães
    Descrição:
        - entender o conceito de objetos através de exemplos
"""

class Veiculo:
    def __init__(self, usuario, maxVelocidade, quilometragem):
        """
            Método construtor da classe Veiculo
            :param usuario: nome do piloto, tipo string
            :param maxVelocidade: velocidade máxima permitida, tipo int
            :param quilometragem: distância percorrida pelo veiculo em km, tipo int
        """
        self.usuario = usuario
        self.maxVelocidade = maxVelocidade
        self.quilometragem = quilometragem
    
    def exibiValores(self):
        """
            Método para imprimi valores no console
        """
        print("Piloto: ", self.usuario)
        print("Velocidade máxima: ", self.maxVelocidade)
        print("Quilometragem: ", self.quilometragem)

#Criando objeto v1
v1 = Veiculo("Iago", 100, 1500)
v1.exibiValores()