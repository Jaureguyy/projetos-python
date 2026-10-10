# Agennda

## Estrutura

### Estrutura de dados
```text
agenda = {                          |                                 |                        |
    dia = {                         |                                 |                        |
        evento = {                  |     agenda = {                  |   eventos = {dados}    |   dados = {
            hora : XXXX             |       dia = { eventos }         |                        |       'data' = XXXX
            descricao: XXXX         |      }                          |                        |       'hora' = XXXX
        }                           |                                 |                        |
    }                               |                                 |                        |
}
```

A estrutura dos dados e informações acontece dentro de dicionários aninhado, os quais são repassados ao arquivo .txt ; Estes dicionários ocorrem na seguinte ordem:

*Agenda* -> *Dias da Semana* -> *Eventos* -> *Informações*.

Enquanto o programa roda, as alterações sempre serão feitas dentro do dicionário. Ao fim de cada operação, a função '*salvar_agenda*' será chamada para salvar as informações no arquivo .txt ; Caso o o programa recém tenha sido iniciado, a função '*carregar_agenda*' será chamada, assim as informações já salvas no arquivo serão "importadas" para dentro do dicionário.

### Dentro do arquivo 'agenda.txt'

Dentro do arquivo .txt , a separação de dias acontece pelo formato: **## dia_semana** ;

Então quando o parsing ocorrer, ele irá diferenciar o '*dia_atual*' através de "##" (jogo da velha) no início da linha.

Já as informações dos eventos, são dispostas da seguinte maneira: **nome_evento|hora|descricao** ; 

Através de laços percorrendo tanto o dicionário como o arquivo, irão inserir/coletar as informações (a depender se vai ser salvo ou carregado).

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
- Migrar o formato de persistência de .txt para .JSON
- Atualização da interface
- Opção de editar eventos
- Melhorar a identificação das entradas (segunda/segunda-feira/Segunda-feira/segunda feira ...)
- Adicionar meses e dias do mês