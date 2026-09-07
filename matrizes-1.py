##Ler 'n' linhas e 'm' colunas de uma matriz, após isso mostrar a soma de todos os elementos.

linhas, colunas = map(int, input("Digite o numero de linhas e colunas da matriz: ").split())
matriz=[] ##Definir a matriz aqui é desnecessário, em vista que a linha da matriz é lida e logo em seguida descartada
soma=0

for i in range(linhas):
    linha = list(map(int,input(f"Digite os valores da linha {i}:").split()))
    matriz.append(linha)
    soma+= sum(linha)

print("Soma da matriz:", soma)