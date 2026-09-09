##Ler um valor e através de uma função declarar o seu fatorial

def fatorial(n):
    resultado=1

    for i in range(1,n+1):
        resultado = resultado*i

    return resultado


x = int(input("Digite um valor: "))

print(fatorial(x))
