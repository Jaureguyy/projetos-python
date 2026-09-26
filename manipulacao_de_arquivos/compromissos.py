"""
Juntando alguns conceitos para a preparação da agenda.
Será feito um arquivo contendo compromissos

"""

# Primeiro será construído dicionários para cada compromisso. Dentro deles terá as seguintes chaves: Data / Hora / Descrição.
# Os valores de cada chave serão fixos, sem nenhum input
# Após serem criados, cada dicionário será inserido no arquivo (1 para cada linha).
# Ou seja, a lógica será: criação/definição no dicionário -> exportar para o arquivo -> cada compromisso dicionário ficará em uma linha

# ------------------------------------------------------

## Construindo 3 dicionários/compromissos e aplicando eles em uma lista:

onibus_manha = {
    'Data' : 'Todos os dias',
    'Hora' : '06:20',
    'Descricao' : 'Pegar ônibus para o trabalho'
}

lanche_manha = {
    'Data' : 'Todos os dias',
    'Hora' : '09:20',
    'Descricao' : 'Fazer lanche matinal'
}

viagem = {
    'Data' : '12/10/2026',
    'Hora' : '02:30',
    'Descricao' : 'Viagem para SC'
}

compromissos = (onibus_manha, lanche_manha, viagem)

# -----------------------------------------------------------

## Jogando cada compromisso no mesmo arquivo (1 compromisso por linha)

with open('compromissos.txt', 'w', encoding='utf-8') as arquivo:
     for compromisso in compromissos:
         arquivo.write((f"{compromisso['Data']} | {compromisso['Hora']} | {compromisso['Descricao']}\n"))

## Dando print do conteudo do arquivo .txt

with open('compromissos.txt', 'r', encoding='utf-8') as arquivo:
     conteudo = arquivo.read()

print(conteudo)