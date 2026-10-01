## Por enquanto a main está sendo utilizada para testes das operações na agenda

from operacoes import adicionar_evento

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


# --------------------------------------------------------
## Adicionando um evento
dia_semana = input("Digite o dia da semana: ")
nome_evento = input("Digite o nome do evento: ")
hora = input("Digite a hora do evento: ")
descricao = input("Descricao do evento:\n")

adicionar_evento(agenda, dia_semana, nome_evento, hora, descricao)

arquivo = open('agenda.txt', 'r')
conteudo = arquivo.read()
arquivo.close()

print(conteudo)
print(f"\n{'-'*30}\n")