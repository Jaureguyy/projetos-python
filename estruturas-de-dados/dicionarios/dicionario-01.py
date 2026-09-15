"""
-Dicionário = { chave : valor, chave2 : valor2, chave3 : valor#}

-Métodos nos dicionários:

1°: .keys(): retorna todas as chaves do dicionário
2°: .values(): retorna todos os valores do dicionário
3°: .items(): retorna os pares -> chave : valor
4°: .get(): acessa a chave de forma segura mesmo que ela não exista
5°: .setdefault(): adiciona chave/valor caso não existam no dicionário

-Percorrendo um dicionário com for:

for chave, valor in pessoa.item():                 ###isto fica semelhante ao desempacotamento de tuplas
    print(f"{chave}: {valor}")

    
-Acessando um dicionário:

dicionario[chave] = valor
dicionario.get(chave, valor)
dicionario.setdefault(chave, valor)

Para diferenciar a utilização do dicionario[chave] = valor e dicionario.setdefault(chave, valor):
O .setedefault() evita que dados sejam sobreescrevidos por engano, já que caso a chave exista, ele não altera nada. Diferente de acessar a chave através de dicionario[chave] = valor
"""