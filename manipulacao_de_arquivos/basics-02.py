"""
Aqui eu irei utilizar o 'with' para fechar automaticamente o .txt

Irei ler a altura de um triangulo e depois escrever dentro do arquivo
"""

# LENDO O TAMANHO
tamanho = int(input("Digite o tamanho do triangulo desejado: "))

# ACESSANDO O ARQUIVO E ESCREVENDO NELE
with open('teste02.txt', 'w') as arquivo:
    colunas=1
    for i in range(tamanho):
        for j in range(colunas):
            arquivo.write('*')
        colunas+=1
        arquivo.write('\n')

# LENDO O ARQUIVO E DEPOIS DANDO PRINT
with open('teste02.txt', 'r') as arquivo:
    conteudo = arquivo.read()

print(conteudo)

