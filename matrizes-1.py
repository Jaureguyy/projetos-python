##Ler 'n' linhas e 'm' colunas de uma matriz, após isso mostrar a soma de todos os elementos.

linhas, colunas = map(int, input("Digite o numero de linhas e colunas da matriz: ").split())
matriz=[]
soma=0

for i in range(linhas):
    linha = list(map(int,input(f"Digite os valores da linha {i}:").split()))
    matriz.append(linha)

for i in range(linhas):
    for j in range(colunas):
        soma+=matriz[i][j]

print("Soma da matriz:", soma)