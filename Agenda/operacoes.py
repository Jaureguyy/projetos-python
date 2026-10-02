'''
@ As atuais operações da agenda: Adicionar evento, remover evento, ler eventos do dia X; Estas mesmas porém referentes a agenda ao todo também serão disponibilizadas (em vista que são mais fáceis por não ter muito parsing)

@ O padrão de variáveis será:

- agenda
- dia_semana
- nome_evento
- hora
- descricao
- operacao (caracteres para cada uma) (mas provavelmente isso será mostrado na main)

@ A estrutura de dados (agenda), será feita na main.py ; para utilizar no código aqui de operações, a agenda será colocada como um argumento em cada função
'''

# -------------------------------------------
##  

# -------------------------------------------
## Função para adicionar evento:

def adicionar_evento(agenda, dia_semana, nome_evento, hora, descricao):
    novo_evento = {
        'hora' : hora,
        'descricao' : descricao
    }
    agenda = agenda[dia_semana].setdefault(nome_evento, novo_evento)

    with open('agenda.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f"{nome_evento}|{hora}|{descricao}")


# --------------------------------------------
## Função para remover eventos

def remover_evento(agenda,dia_semana, nome_evento):
    agenda[dia_semana].pop(nome_evento)
    with open('agenda.txt', 'w', encoding='utf-8') as arquivo:
        for dia, eventos in agenda.items():
            for nome_evento, dados in eventos.items():
                arquivo.write(f"{nome_evento}|{dados['hora']|dados['descricao']}\n")