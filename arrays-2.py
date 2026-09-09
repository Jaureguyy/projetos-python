##Ler uma lista de tamanho variável, depois apresentar o maior e menor valor pertencentes a ela

array = list(map(int, input().split()))
maior=array[0]
menor=array[0]

for i in array:
    if i > maior:
        maior=i

    if i < menor:
        menor=i


print("Maior valor:", maior)
print("Menor valor:", menor)