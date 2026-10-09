import json

# Alguns testes com o json

# ------------------------------------------------------

## Jogando uma string

string = input("- Escreva uma string para colocar no json:\n\n")

with open('teste.json', 'w', encoding='utf-8') as arquivo:
    json.dump(string, arquivo, indent=4, ensure_ascii=False)

with open('teste.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

print(dados)
print(f"\n{'-'*30}\n")

## Jogando uma lista

lista = list(input("Digite uma lista qualquer:\n\n").split())

with open('teste.json', 'w', encoding='utf-8') as arquivo:
    json.dump(lista, arquivo, indent=4, ensure_ascii=False)   ## Sem o indent ele printa a lista em uma única linha

with open('teste.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

print(type(dados))
print(dados)
print(f"\n{'-'*30}\n")

# Testando o 's' no final

texto = json.dumps({'valor':1000})   # Sem o 's' ele gera erro
print(type(texto))
print(f"{texto}\n")

lista = json.dumps([1, 2, 3, 4, 5])
print(f"Print do tipo da variável 'lista': {type(lista)}")
print(f"Print do json.load: {json.loads(lista)}")

# Enviando uma tupla ao JSON

coordenadas = ('x', 'y')

with open('teste.json', 'w', encoding='utf-8') as arquivo:
    json.dump(coordenadas, arquivo)

with open('teste.json', 'r', encoding='utf-8') as arquivo:
    coordenadas = json.load(arquivo)

print(type(coordenadas))