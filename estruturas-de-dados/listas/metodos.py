#Ler uma lista e depois: aprensentar a lista inteira; ordena-la; remover o maior valor; inserir o número '0' na primeira posição;
#imprimir a lista final

##Leitrura e apresentação da lista inicial
lista = list(map(int,input("Digite os valores da lista: ").split()))
print("Valores iniciais da lista:", lista)
print(f"\n{"-"*30}\n")

##Ordenação da lista através de .sort :
lista.sort()
print("Lista ordenada:", lista)
print(f"\n{"-"*30}\n")

##Removendo o maior valor :
lista.remove(max(lista))
print("Lista sem o maior valor:", lista)
print(f"\n{"-"*30}\n")

##Inserindo o número '0' no início da lista
lista.insert(0,0)
print("Valor '0' no inicio da lista:", lista)
print(f"\n{"-"*30}\n")

##Imprimindo a lista final
print("Lista final:", lista)