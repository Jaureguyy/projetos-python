## Por enquanto a main está sendo utilizada para testes das operações na agenda

import operacoes

# ----------------------------------------------------
## Estrutura de persistência

"""
agenda = {
    dia = {
        evento = {
            hora : XXXX
            descricao: XXXX
        }    
    }
}
"""

agenda = {
    'domingo' : {},
    'segunda' : {},
    'terca' : {},
    'quarta' : {},
    'quinta' : {},
    'sexta' : {},
    'sabado' : {}
}

# -------------------------------------------------------
## Carregando o evento


agenda = operacoes.carregar_agenda(agenda)

print(f"\n{'-'*30}\n")
print(agenda)

arquivo = open('agenda.txt', 'r', encoding='utf-8')
conteudo = arquivo.read()
arquivo.close()
print(conteudo)


# --------------------------------------------------------
## Adicionando um evento
# dia_semana = input("Digite o dia da semana: ")
# nome_evento = input("Digite o nome do evento: ")
# hora = input("Digite a hora do evento: ")
# descricao = input("Descricao do evento:\n")

# operacoes.adicionar_evento(agenda, dia_semana, nome_evento, hora, descricao)

# arquivo = open('agenda.txt', 'r')
# conteudo = arquivo.read()
# arquivo.close()

# print(conteudo)
# print(f"\n{'-'*30}\n")

# ---------------------------------------------------------
## Removendo um evento

# dia_semana = input("Digite o dia do evento que será removido: ")
# nome_evento = input("Digite o nome do evento que será removido: ")

# operacoes.remover_evento(agenda, dia_semana, nome_evento)

# arquivo = open('agenda.txt', 'r')
# conteudo = arquivo.read()
# arquivo.close()

# print(conteudo)
# print(f"\n{'-'*30}\n")

# ----------------------------------------------------------
## Lendo os eventos de um dia em específico

