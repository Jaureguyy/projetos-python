"""
Salvar infos - json.dump(dados, arquivo)
Carregar infos - json.load(arquivo)

Parâmetros importantes: 

# indent=4 ; Deixa o arquivo identado e legível
# ensure_ascii=False ; Mantém os acentos para que eles não fiquem ilegíveis dentro do arquivo
"""

# Criando um .json com 3 níveis

import json

## Dicionário
agenda = {
    'segunda' : {},
    'terca' : {},
    'quarta' : {},
    'quinta' : {},
    'sexta' : {},
    'sabado' : {},
    'domingo' : {}
}

## Modificando dicionário
dia_semana = input("Digite um dia da semana para adicionar um evento: ")
nome_evento = input('Escreva o nome do evento: ')
hora = input('Digite a hora do evento: ')
descricao = input('Escreva a descrição do evento: ')

novo_evento = {
    'hora' : hora,
    'descricao' : descricao
}

agenda[dia_semana].setdefault(nome_evento, novo_evento)


# Inserindo as informações no json
with open('teste.json', 'w', encoding='utf-8') as arquivo:
    json.dump(agenda, arquivo, indent=4, ensure_ascii=False)

## Lendo o json
with open('teste.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

print(dados)