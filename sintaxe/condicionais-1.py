##Ler tres valores, imprimir "Triangulo valido" se eles puderem formar os lados de um triangulo, caso ao contrario imprimir "Triangulo invalido"

a, b, c = map(int, input().split())


if a==0 or b==0 or c==0:
    print("Triangulo invalido")
elif a+b > c and a+c > b and b+c > a:
    print("Triangulo valido")
else:
    print("Triangulo invalido")
