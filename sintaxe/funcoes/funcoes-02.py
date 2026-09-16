#Função que retorna mais de um valor é teoricamente o mesmo processo que um desempacotamento de uma tupla.
#Retorna uma tupla = (x, y) ; porém em duas variáveis

#Fazer uma função "estatísticas" que possui uma lista como parâmetro e devolve o maior, menor valor e a média

def estatisticas(lista):
    maior = lista[0]
    menor = lista[0]

    for i in lista:
        if i>maior:
            maior=i

        if i<menor:
            menor=i

    media = sum(lista)/len(lista)

    return maior, menor, media


lista = list(map(int, input(f"Digite os valores da lista: ").split()))

print(estatisticas(lista))