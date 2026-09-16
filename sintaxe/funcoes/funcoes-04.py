#Funções que utilizam: *args

#A escolha entre *args ou uma lista como parâmetro irá variar da origem dos dados. Caso as informações vierem de algum arquivo ou algo "pronto", é mais viável utilizar uma lista. Já para o cenário em as informações vem soltas, *args pode ser utilizado

#Função "estatísticas" que retorna o maior e menor valor, também a média. Utilizar *args como parâmetro

def estatisticas(*numeros):
    maior = numeros[0]
    menor = numeros[0]

    for i in numeros:
        if i>maior:
            maior=i

        if i<menor:
            menor=i

    media = sum(numeros)/len(numeros)

    return maior, menor, media

valores = list(map(int, input("Digite um quantidade de valores para saber suas estatisticas:\n").split()))

maior, menor, media = estatisticas(*valores)

print(f"\nMaior valor: {maior}")
print(f"Menor valor: {menor}")
print(f"Media dos valores: {media}")


## ++ alguns conceitos como + de 1 retorno na função e desempacotamento