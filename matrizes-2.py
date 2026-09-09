##Ler uma matriz e demonstrar a soma de sua diagonal principal

### 1 Loop será para a leitura da matriz, o 2° para a soma

linhas, colunas = map(int,input("Digite o numero de linhas e colunas da matriz: ").split())
matriz=[]
soma=0

for i in range(linhas):
    linha = list(map(int,input(f"Digite os valores da linha {i}: ").split()))
    matriz.append(linha)


for i in range(linhas):
    for j in range(colunas):
        if i==j:
            soma+=matriz[i][j]

print("A soma da diagonal principal eh:", soma)