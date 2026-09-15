#Múltiplos parâmetros com valores padrão
#Regra importante: um parâmetro com valor padrão só pode ir após um sem, nunca antes:
# def funcao(a, b, c=10)  -> OK
# def funcao(a, b=10, c)  -> X

#Ler uma função para calcular a potêncio, a qual recebe uma base e um expoente com valor padrão =2

def potencia(valor, expoente=2):
    base=valor
    for i in range(expoente-1):
        valor*=base

    return valor

base = int(input("Digite a base da potencia: "))
expoente = int(input("Defina um expoente para a potencia: "))

print(f"Resultado da potencia: {potencia(base, expoente)}")