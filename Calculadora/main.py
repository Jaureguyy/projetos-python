"""
Com o dispatcher criado, agora basta inicializar com 2 valores e 1 operação. Inicialmente o primeiro valor será inicializado junto do segundo, porém posteriormente ele se tornará o resultado e será reaproveitado. Dentro de um while será viável"""

## Import do dispatcher

from operacoes import dispatcher


## Inicializar os 2 valores + operação fora do while

calculo = input("\nDigite dois valoes e a operacao desejada\nFORMATO VALIDO: NUMERO OPERACAO NUMERO\n\n->")
valor1, operacao, valor2 = calculo.split()

