"""
    dicionarios.py
    Autor: Iago Magalhães
    Descrição:
        - Mostrar exemplos de como declarar dicionários em Python
"""

#Dicionários
myDict = {
    "Disciplina": "Supervisório",
    "Ano": 2022
}
print(myDict)
print("Obtém o valor da chave 'Ano:'", myDict["Ano"])
print("Obtém uma lista das chaves:", myDict.keys())
myDict["Semestre"] = 6 #adiciona dado na lista
print("Novo dado no dicionário", myDict)
myDict["Ano"] = 2022.1
print("Atualiza 'Ano'", myDict)
myDict.pop("Ano")
print("Remove dado do dicionário", myDict)