"""
    construtores.py
    Autor: Iago Magalhães
    Descrição:
        - class Veiculo
        - Instancia objeto da classe Veiculo
        - Utilizar método contrustor __init__
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

v1 = Veiculo("Iago", 100, 1500)
v1.exibiValores()