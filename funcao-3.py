##Ler três valores e através de uma função retornar qual é o maior
##Acabei fazendo um mini bubble sort

def maior(a,b,c):
    if a<b:
        auxiliar=a
        a=b
        b=auxiliar

    if b<c:
        auxiliar=b
        b=c
        c=auxiliar

    if a<b:
        auxiliar=a
        a=b
        b=auxiliar

    return a


x, y, z = map(int, input().split())
print(maior(x, y, z))