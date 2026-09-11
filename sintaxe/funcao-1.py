##Ler um valor e através de uma função dar true se é par, false caso seja ímpar

def ehPar(a):
    return a%2==0


x = int(input("Digite um valor: "))

if ehPar(x):
    print("Este valor eh par")
else:
    print("Este valor eh impar")