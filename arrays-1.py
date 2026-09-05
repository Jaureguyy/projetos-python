##Ler um array e logo em seguida apresentar a soma de seus números

lista = list(map(int, input().split()))
soma=0

for i in lista:
    soma+=i

print(soma)