"""
Para a calculadora eu irei utilizar um dispatcher. Vi em um breve vídeo a utilização de um ("https://www.youtube.com/watch?v=eo-9Gd1tkFI&t=666s"), então farei de forma similar para processar as operações.
Terei que juntar o dispatcher com uma maneira de processar vários cálculos de uma vez, mas isso provavelmente será resolvido na main
"""
##

"""
Primeiro irei fazer as funções das operações de maneira separada para depois colocar na função de dispatcher
"""

## Cada função receberá 2 valores (a identificação da operação será feita através da chave do dispatcher). Um dos valores será dado antes de iniciar o while da calculadora, após isso ele será o "resultado" da operação anterior para poder reaproveitar em vários cálculos subsequentes. Assim o segundo valor sempre será um novo a cada loop.

def soma(valor,valor2):
    return valor + valor2

def subtracao(valor, valor2):
    return valor - valor2

def multiplicacao(valor, valor2):
    return valor - valor2

def divisao(valor, valor2):
    return valor / valor2

def invalida(valor, valor2):
    return None 


def dispatcher(valor, valor2, simbolo):
    operacoes = {
        '+' : soma,
        '-' : subtracao,
        '*' : multiplicacao,
        '/' : divisao
    }

    operacao = operacoes.get(simbolo, invalida)
    return operacao(valor, valor2)



## Funções e dispatcher criados. 
## Cada função tem 2 valores e o dispatcher é acrescentado a variável "simbolo" que seria o char/string que representa a chave de tal operação.
## A variável "operacao" dentro do dispatcher é utilizada para puxar o símbolo da operação e de acordo com o que vir, irá virar a operação/função.

