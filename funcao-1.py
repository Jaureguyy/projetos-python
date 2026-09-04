##Ler um valor e através de uma função dar true se é par, false caso seja ímpar

def ehPar(a):
    if a%2==0:
        return True
    else:
        return False


x = int(input("Digite um valor: "))

if ehPar(x)==True:
    print("Este valor eh par")
else:
    print("Este valor eh impar")