"""
Abrindo um arquivo:    arquivo = open("nome.txt", "w")

-O primeiro argumento sempre será o nome/caminho do arquivoo. Já o segundo é o 'modo de abertura', estes podem ser:

'w' -> abre para escrever, caso não exista ele cria escrevendo algo novo. Para o caso de já existir, apaga tudo e começa do 0
'a' -> (append) abre para adicionar ao final, sem apagar os dados anteriores
'r' -> abre para ler

"""

# ESCREVENDO UM ARQUIVO
arquivo = open("teste01.txt", "w")
arquivo.write("VAMOOOOOOOO\n")
arquivo.write("VAMOOOOOOOOO 02")

## Neste modo de abertura é essencial fechar o arquivo no final, caso não aconteça é possível perder tudo - isto serve para arquivo=open("...", "...")
arquivo.close()

# LENDO UM ARQUIVO
arquivo = open("teste01.txt", "r")
conteudo = arquivo.read()
arquivo.close()

print(f"{conteudo}\n")

# ADICIONANDO ALGO NO FINAL DO ARQUIVO (append)
arquivo = open("teste01.txt", "a")
arquivo.write("\nVAMMMMOOOOOO 03")
arquivo.close()

## Lendo para a demonstração
arquivo = open('teste01.txt', 'r')
conteudo = arquivo.read()
arquivo.close()

print(conteudo)

# "LIMPANDO" O ARQUIVO
arquivo = open('teste01.txt', 'w')
arquivo.write("VAZIO")
arquivo.close()

## Lendo para demonstração
arquivo = open('teste01.txt', 'r')
conteudo = arquivo.read()
arquivo.close()

print(f"\n{conteudo}")
