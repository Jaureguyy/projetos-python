#Ler uma lista e após isso: ordena-la; pegar apenas a parte de trás da lista; na nova lista remover o menor valor;
#inserir o número '100' ao final da lista; imprimir a lista final


##Leitura e apresentação da lista inicial
lista = list(map(int,input("Digite os valores da lista: ").split()))
print(f"\nLista inicial: {lista}\n{'-'*30}\n")

##Ordenando a lista : 
lista.sort()
print(f"Lista ordenada: {lista}\n{'-'*30}\n")

##Pegando apenas a primeira parte da lista
lista = lista[0:len(lista)//2]
print(f"Lista apenas com a primeira metade: {lista}\n{'-'*30}\n")

##Removendo o menor valor da lista
lista.remove(min(lista))
print(f"Lista sem o menor valor: {lista}\n{'-'*30}\n")

##Adicionando o valor '100' ao final da lista
lista.append(100)
print(f"Lista com o valor '100' no final: {lista}\n{'-'*30}\n")

##Lista final
print(f"Lista final: {lista}")