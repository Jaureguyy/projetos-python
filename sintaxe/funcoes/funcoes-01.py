#Múltiplos parâmetros com valores padrão
#Regra importante: um parâmetro com valor padrão só pode ir após um sem, nunca antes:
# def funcao(a, b, c=10)  -> OK
# def funcao(a, b=10, c)  -> X

#Ler uma função para calcular a potêncio, a qual recebe uma base e um expoente com valor padrão =2

def potencia(base, expoente=2):
    valor=base
    for i in range(expoente-1):    ##  -1 por conta que "valor" já conta como base 1
        valor*=base

    return valor

base = int(input(f"Digite o valor da base: "))
expoente = int(input(f"Defina o valor do expoente: "))

print(potencia(base, expoente))