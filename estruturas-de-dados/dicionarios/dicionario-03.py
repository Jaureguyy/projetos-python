#Criar um dicionario referente ao cadastro de um aluno (sem input novamente).
#Deve conter: nome, idade, notas, endereço (outro dicionário)
#Após isso: imprimir nome e cidade; calcular a média das notas; adicionar uma nota nova; adicionar o país; imprimir tudo ao final

aluno = {
    "nome" : "Raimundo",
    "idade" : 9,
    "notas" : [10, 3, 2, 5, 5],
    "endereco" : {
        "cidade" : "Epitaciolandia",
        "Estado" : "Acre"
    }
}

#Imprimindo nome e cidade
print("\n")
print(f"Nome do aluno: {aluno.get('nome')}")
print(f"Cidade do aluno: {aluno['endereco']['cidade']}")
print(f"\n{'-'*30}\n")

#Calculando e imprimindo a média das notas
soma=0
for nota in aluno['notas']:
    soma+=nota

print(f"Media do aluno: {soma/len(aluno['notas'])}")
print(f"\n{'-'*30}\n")

#Adicionando uma nova nota ; Por ser uma lista, utiliza-se .append()
aluno["notas"].append(10)
print(f"Nota do exame: {aluno['notas'][-1]}")
print(f"Nova media: {sum(aluno['notas'])/len(aluno['notas'])}")
print(f"\n{'-'*30}\n")

#Adicionar o país -> No dicionário aninhado
aluno["endereco"]["pais"] = "Brasil"

#Printando o dicionário por completo
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")