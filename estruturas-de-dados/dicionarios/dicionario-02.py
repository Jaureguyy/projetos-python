#Criar um dicionário para um produto, contendo informações como: nome, preço e quantidade. 
#Será sem input, apenas irei criar e após isso apresentar os valores de forma separada e posteriormente os pares


produto = {
    "nome" : "Tanque de Guerra",
    "preco" : 50.000,
    "quantidade" : 1
}

#Apresentando os valores de forma separada
print(f"Nome do produto: {produto.get("nome")}")
print(f"Valor do produto: {produto.get("preco")}")
print(f"Quantidade de produtos: {produto.get("quantidade")}")

print(f"\n{'-'*30}\n")

#Utilizando get em uma chave inexistente
print(f"Endereco de entrega: {produto.get('endereco_de_entrega', 'rua Brasil')}")
print(f"\n{'-'*30}\n")

#Apresentando os pares
for chave, valor in produto.items():            ##Neste caso o endereço de entrega não existe pois ele não foi add no dicionario 
    print(f"{chave}: {valor}")                  ##Para que realmente a chave/valor sejam adicionados caso não existam, é
                                                ##necessário utilizar .setdefault('chave', 'valor') ou dicionario[chave] = valor
print(f"\n{'-'*30}\n")

#Adicionando definitivamente o endereço de entrega + responsavel -> rodando um novo loop para comprovar
produto.setdefault("endereco_de_entrega", "rua Brasil")
produto["responsavel"] = "Ratatui"

for chave, valor in produto.items():
    print(f"{chave}: {valor}")