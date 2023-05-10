"""
    estruturas_condicionais.py
    Autor: Iago Magalhães
    Descrição:
        - Mostrar exemplos de como utilizar estruturas condicionais em Python
"""

nome = 'Iago'
idade = 23

#Estrutura condicional básica, apenas com if e else
if(nome == 'Iago'):
    print('Oi', nome)
else:
    print('Não te conheço!')

#Estrutura condicional utilizando elif
if(idade < 18):
    print('Menor de idade')
elif(idade >= 18):
    print('Maior de idade')
else:
    print('Erro!')