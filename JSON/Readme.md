# JSON

## Tópicos objetivos:
    - JSON significa JavaScript Object Notation (notação de objeto JavaScript). É um formato de texto para armazenar e transmitir dados.
   - Criar um objeto
   - Transformar um objeto em uma string
   - Transformar uma string em objeto
   - Manipular um objeto

## JSON em Python

### Lib
    import json

### Analisar JSON - Converter de JSON para Python
Se você tiver uma string JSON, poderá analisá-la usando o json.loads()método.

- Exemplo: Converter de JSON para Python
    import json

    #some JSON:
    x =  '{ "name":"John", "age":30, "city":"New York"}'

    #parse x:
    y = json.loads(x)

    #the result is a Python dictionary:
    print(y["age"])

### Converter de Python para JSON
Se você tiver um objeto Python, poderá convertê-lo em uma string JSON usando o json.dumps()método.
- Exemplo 01: Converter de Python para JSON
    import json

    #a Python object (dict):
    x = {
    "name": "John",
    "age": 30,
    "city": "New York"
    }

    #convert into JSON:
    y = json.dumps(x)

    #the result is a JSON string:
    print(y)

- Exemplo 02: Converta um objeto Python contendo todos os tipos de dados legais
    import json

    x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann","Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
    }

    print(json.dumps(x))

### Formatar o resultado
O exemplo acima imprime uma string JSON, mas não é muito fácil de ler, sem recuos e quebras de linha.

O json.dumps()método possui parâmetros para facilitar a leitura do resultado:

- Exemplo 01: Use o indentparâmetro para definir os números de recuos
    json.dumps(x, indent=4)

- Exemplo 02: Use o separatorsparâmetro para alterar o separador padrão
    json.dumps(x, indent=4, separators=(". ", " = "))

- Exemplo 03: Use o sort_keysparâmetro para especificar se o resultado deve ser classificado ou não
    json.dumps(x, indent=4, sort_keys=True)

## Referências
- https://www.w3schools.com/python/python_json.asp