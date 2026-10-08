import operacoes

# ----------------------------------------------------
## Estrutura de persistência

"""
agenda = {                          |                                 |                        |                 
    dia = {                         |                                 |                        |
        evento = {                  |     agenda = {                  |   eventos = {dados}    |   dados = {
            hora : XXXX             |       dia = { eventos }         |                        |       'data' = XXXX
            descricao: XXXX         |      }                          |                        |       'hora' = XXXX
        }                           |                                 |                        |
    }                               |                                 |                        |
}                                   |                                 |                        |
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

# ---------------------------------------------
## 

try:
    operacoes.carregar_agenda(agenda)
    print(f"\n\n{'-'*12}AGENDA{'-'*12}\n")

except FileNotFoundError:
    print("Ageda Vazia . . . . . .\n\n")
    with open('agenda.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write("Agenda Vazia . . . . . . (cri cri cri cri)")

while True:
    print("Escolha uma opção:\n")
    operacao = input("[1] - Adicionar Evento\n[2] - Remover Evento\n[3] - Ler Eventos\n[4] - Ler Agenda\n[5] - Salvar e Sair\n\n->")

    if operacao == '1':
        print(f"[{operacao}] - Adicionar Evento:\n")

        dia_semana = input("Digite o dia da semana: ")
        nome_evento = input("Escreva o nome do evento: ")
        hora = input("Digite a hora do evento: ")
        descricao = input("Descricao do evento: ")

        operacoes.adicionar_evento(agenda, dia_semana, nome_evento, hora, descricao)
        operacoes.salvar_agenda(agenda)

        print(f"\nEvento adicionado com sucesso!")

    elif operacao == '2':
        print(f"[{operacao}] - Remover Evento:\n")

        dia_semana = input("Escreva o dia do evento que será removido: ")
        nome_evento = input("Digite o nome do evento: ")

        operacoes.remover_evento(agenda, dia_semana, nome_evento)
        operacoes.salvar_agenda(agenda)

        print("\nEvento removido com sucesso!")

    elif operacao == '3':
        print(f"[{operacao}] - Ler Eventos:\n")

        dia_semana = input("Escreva o dia da semana para ler os seus eventos: ")
        
        operacoes.ler_eventos(agenda, dia_semana)

    elif operacao == '4':
        print(f"[{operacao}] - Ler Agenda:\n")

        operacoes.ler_agenda()

    elif operacao == '5':
        print(f"[{operacao}] - Salvar e Sair:\n")

        operacoes.salvar_agenda(agenda)

        print("\nAgenda Salva com sucesso!")
        break