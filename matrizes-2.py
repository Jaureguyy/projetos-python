##Ler uma matriz e demonstrar a soma de sua diagonal principal

### 1 loop irá ler a linha (não vai salvar na matriz) e ao mesmo tempo irá somar o valor da diagonal principal (fazendo através de i==posição da diagonal principal)

linhas, colunas = map(int,input("Digite o numero de linhas e colunas da matriz: ").split())
soma=0

for i in range(linhas):
    linha = list(map(int,input(f"Digite os valores da linha {i}: ").split()))
    soma+=linha[i]

print("A soma da diagonal principal eh:", soma)