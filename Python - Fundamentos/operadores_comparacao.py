"""
    operadores_comparacao.py
    Autor: Iago Magalhães
    Descrição:
        - Mostrar exemplos de como utilizar operadores de comparação em Python
"""

#Exemplos de operadores aritméticos
numero_1 = 5
numero_2 = 2

soma = numero_1 + numero_2
subtracao = numero_1 - numero_2
multiplicacao = numero_1 * numero_2
divisao = numero_1 / numero_2
divisao_inteira = numero_1 // numero_2
modulo = numero_1 % numero_2
exponenciacao = numero_1 ** numero_2

print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(divisao_inteira)
print(modulo)
print(exponenciacao)


#Exmplos de operadores de atribuição
numero_1 = 5
numero_2 = 5

numero_1 += 5 #Adição
print(numero_1)

numero_2 -= 2 #Subtração
print(numero_2)

numero_1 *= 2 #Multiplicação
print(numero_1)

numero_2 /= 3 #Divisão
print(numero_2)

numero_1 %= 2 #Resto
print(numero_1)


#Exemplos de operadores comparação
numero_1 = 2
numero_2 = 4

soma = numero_1 + numero_2

if soma > 10: #> (Maior que)
    print("soma é maior que 10")
else:
    print("soma não é maior ou igual a 10")

if soma < 10: #< (Menor que)
    print("soma é menor que 10")
else:
    print("soma é maior ou igual a 10")

if soma == 10: #== (Igual a)
    print("soma é igual a 10")
else:
    print("soma não é igual a 10")

if soma != 10: #!= (Diferente de)
    print("soma é diferente de 10")
else:
    print("soma é igual a 10")

if soma >= 10: #>= (Maior ou igual a)
    print("soma é maior ou igual a 10")
else:
    print("soma não é maior ou igual a 10")

if soma <= 10: #<= (Menor ou igual a)
    print("soma é menor ou igual a 10")
else:
    print("soma não é maior ou igual a 10")


#Exemplos de operadores lógicos
idade_lucas = 21
idade_carolina = 19

# OPERADOR OR
if idade_lucas >= 18 or idade_carolina >= 18:
    print("Pelo menos um dos dois é maior de idade")
else:
    print("Lucas e Carolina não são maiores de idade")

# OPERADOR AND
if idade_lucas >= 18 and idade_carolina >= 18:
    print("Lucas e Carolina são maiores de idade")
else:
    print("Pelo menos um dos dois não é maior de idade")


#Exemplos de operadores de identidade
time_carlos = 'Botafogo'
time_luciano = 'Flamengo'
time_fabricia = 'Botafogo'

if time_carlos is time_luciano:
    print("time_carlos - time_luciano = mesmo objeto")
else:
    print("time_carlos - time_luciano = objetos diferentes")

if time_carlos is not time_fabricia:
    print("time_carlos - time_fabricia = mesmo objeto")
else:
    print("time_carlos - time_fabricia = objetos diferentes")


#Exemplos de operadores de associação
frutas = ["banana","laranja","uva","ameixa"]

fruta_1 = "ameixa"
fruta_2 = "melancia"

print(fruta_1 in frutas) # True
print(fruta_2 not in frutas) # True