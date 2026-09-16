#Ler uma lista e apresentar: 3 primeiros valores, três últimos elementos, lista inteira sem os elementos dos extremos


##Leitura e apresentação da lista inteira
lista = list(map(int,input("Digite os valores da lista: ").split()))
print("Valores da lista:", lista)

##Slicing para aprensentar as solicitações
print("Tres primeiros valores da lista:", lista[:3])
print("Tres ultimos elementos da lista:", lista[-3:])
print("Lista inteira sem os elementos dos extremos:", lista[1:-1])