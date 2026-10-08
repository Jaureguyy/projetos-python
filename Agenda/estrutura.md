# Estrutura + Ideias para a agenda

## Estrutura
**Estrutura geral:** Inicialmente a agenda será semanal, um dicionário para cada dia da semana. Dentro de cada dia haverá *eventos*, os quais terão *hora* e *descricao* como chaves.

Logo no início do programa o .txt é carregado através de *carregar_agenda* para 'importar' as informações para o dicionário **agenda**. Após a inicialização, toda alteração é feita no dicionário e salvada com *salvar_agenda* dentro do .txt . 

## Operações
Na agenda as seguintes operações estão disponíveis:
### Adicionar Evento

Recebe como argumento *dia_semana*, *nome_evento*, *hora* e *descricao*. Após isso cria o dicionário **novo_evento** e faz um .setdefault() na agenda (dicionário).

### Remover Evento

Possui como parâmetro *dia_semana* e *nome_evento* para remover da agenda (dicionário).

### Ler Eventos

Faz a leitura dos eventos de um dia da semana em específico. 

### Ler Agenda

Realiza uma leitura completa da agenda. Esta função diferentemente da anterior, percorre o arquivo .txt invés do dicionário. Esta escolha foi efetuada por conta de casos quando o arquivo não existe e é escrito "Vazio" dentro dele.

### Salvar e Carregar

- salvar_agenda

Sempre que uma mudança é realizada no dicionário, automaticamente ele salva no .txt

- carregar_agenda

Utilizada para 'importar' as informações do .txt para dicionário.




## Ideias futuras
~~*building*~~