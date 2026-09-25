"""
O enumerate serve para numerar itens enquanto percorre um iterável que retorna pares, semelhante ao que já foi utulizado em dicionários
"""

professores = ['Maria', 'Fábio', 'Mario', 'Adi']
print('\n')
for indice, professor in enumerate(professores): ##É possível fazer-> enumerate(professores, start=1);para poder definir o inicio
    print(f"{indice} : {professor}")

"""
O que ele faz é percorrer algo e numerar o primeiro valor do par como no exemplo acima
"""

print(f"\n{'*'*30}\n")

alunos = ['Zézinho', 'Robinson', 'Batman', 'Jhony Bravo', 'Mary Jane']
for index, aluno in enumerate(alunos, start=1):  #Utilizando o "start"
    print(f"{index} : {aluno}")

print(f"\n{'*'*30}\n")

# JOGANDO ISSO EM UM ARQUIVO + ENCODING + LEITURA  
with open("alunos_e_professores.txt", 'w', encoding='utf-8') as arquivo:
    for professor in professores:
        arquivo.write(f"{professor}\n")
with open("alunos_e_professores.txt", 'a', encoding='utf-8') as arquivo:
    for aluno in alunos:
        arquivo.write(f"{aluno}\n")

with open('alunos_e_professores.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()

print(f"CONTEUDO DO ARQUIVO:\n{conteudo}")
print(f"\n{'*'*30}\n")

# REPRESENTANDO JUNTO DO ENUMERATE

with open('alunos_e_professores.txt', 'r', encoding='utf-8') as arquivo:
     for index, pessoa in enumerate(arquivo, start=1):
          print(f"{index} : {pessoa.strip()}")