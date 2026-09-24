"""
O try/except funciona semelhante a um if/else para casos em que o programa quebra
Primeiro ele executa o try, caso gere o erro informado ele executará o except


try:
    bloco
except ERRO_X:
    bloco

"""

# Ler um arquivo inexistente que irá gerar o erro "FileNotFoundError" e executar um except para este problema

## Gerando o erro para teste:
"""
with open('dados_inexistentes', 'r') as arquivo:
    conteudo = arquivo.read()
"""

# Utilizando o try/except:
try:
    with open('dados_inexistentes.txt', 'r') as arquivo:
        conteudo = arquivo.read()
    print(conteudo)

except FileNotFoundError:
    print("ARQUIVO INEXISTENTE | GERANDO NOVOS DADOS")
    with open('dados_inexistentes.txt', 'w') as arquivo:
        arquivo.write("LINHA 01")

    with open('dados_inexistentes.txt', 'r') as arquivo:
        conteudo = arquivo.read()
    print(f"\nNOVOS DADOS:")
    print(conteudo)

# TESTANDO UM INPUT NO WRITE

with open('dados_inexistentes.txt', 'a') as arquivo:
    arquivo.write(input("\nDigite o conteudo da linha 02:\n"))

with open('dados_inexistentes.txt', 'r') as arquivo:
    novo_conteudo = arquivo.read()

print(f"Novo conteudo do arquivo:\n\n{novo_conteudo}")