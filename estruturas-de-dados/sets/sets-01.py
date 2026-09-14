##Os sets são coleções sem ordem definida, não permitem duplicatas, são mutáveis(com métodos próprios)
##Na sintaxe os sets são definidos utilizando chaves "{}"
##Por conta de não permitirem duplicatas, podem ser utilizados em operações matemáticas como: união('|'), interseção('&') e diferença('-').

#Ler duas listas de valores, transforma-las em sets e depis imprimir: a interseção, união e os valores que estão no primeiro conjunto mas não no segundo

lista01 = list(map(int,input("Digite os valores da primeira lista: ").split()))
lista02= list(map(int,input("Digite os valores da segunda lista: ").split()))

print(f"\n{'-'*30}\n")

print(f"Estes sao os valores da lista 01: {lista01}\nEstes sao os valores da lista 02: {lista02}\n{'-'*30}\n")

set01 = set(lista01)
set02 = set(lista02)

##Uniao
print(f"Uniao: {set01|set02}\n")
##Interseção
print(f"Intersecao: {set01&set02}\n")
##Valores do primeiro conjunto e que não estão no segundo
print(f"A-B: {set01-set02}\n")