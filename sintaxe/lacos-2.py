#Laço de repetição while: ler vários números inteiros e fazer a soma de todos. O loop deve parar quando n==0

n = int(input("Digite um valor: "))
soma=0

while n>0:
    soma+=n
    n = int(input("Digite um valor "))

print("Soma:", soma)