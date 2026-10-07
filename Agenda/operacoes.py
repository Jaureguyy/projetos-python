'''
@ As atuais operações da agenda: Adicionar evento, remover evento, ler eventos do dia X, carregar agenda, salvar agenda, ler agenda (inteira).

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
## Função para carregar a agenda
def carregar_agenda(agenda):
    with open('agenda.txt', 'r', encoding='utf-8') as arquivo:
        dia_atual = None
        for linha in arquivo:
            if linha.startswith('##'):
                dia_atual = linha.replace('##', '').strip()
            else:
                nome_evento, hora, descricao = linha.strip().split("|")
                novo_evento = {
                    'hora' : hora,
                    'descricao' : descricao
                }
                agenda.setdefault(dia_atual,)
                agenda[dia_atual].setdefault(nome_evento, novo_evento)

# ------------------------------------------
## Função para salvar a agenda
def salvar_agenda(agenda):
    with open('agenda.txt', 'w', encoding='utf-8') as arquivo:
        for dia, eventos in agenda.items():
            arquivo.write(f"## {dia}\n")
            for nome_evento, dados in eventos.items():
                arquivo.write(f"{nome_evento}|{dados['hora']}|{dados['descricao']}\n")

# -------------------------------------------
# Função para adicionar evento:
def adicionar_evento(agenda, dia_semana, nome_evento, hora, descricao):
    novo_evento = {
        'hora' : hora,
        'descricao' : descricao
    }
    agenda[dia_semana].setdefault(nome_evento, novo_evento)

# --------------------------------------------
# Função para remover eventos

def remover_evento(agenda,dia_semana, nome_evento):
    agenda[dia_semana].pop(nome_evento)

# -----------------------------------------------
## Ler eventos de um dia em específico
def ler_eventos(agenda, dia_semana):
    print(f"Eventos de {dia_semana}:\n")
    if agenda[dia_semana]:
        for nome_evento, dados in agenda[dia_semana].items():
            print(f"{nome_evento}|{dados['hora']}|{dados['descricao']}")
    else:
        carregar_agenda(agenda)
        for nome_evento, dados in agenda[dia_semana].items():
            print(f"{nome_evento}|{dados['hora']}|{dados['descricao']}")

# ------------------------------------------------
## Ler a agenda
def ler_agenda():
    with open('agenda.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
    print(conteudo)
