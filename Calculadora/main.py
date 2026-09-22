"""
Com o dispatcher criado, agora basta inicializar com 2 valores e 1 operação. Inicialmente o primeiro valor será inicializado junto do segundo, porém posteriormente ele se tornará o resultado e será reaproveitado. Dentro de um while será viável

Atualmente só existem as operações: '+' ; '-' ; '*' e '/' (divisão)
"""

## Import do dispatcher

from operacoes import dispatcher


## Inicializar os 2 valores + operação fora do while

calculo = input("\nDigite dois valoes e a operacao desejada\nFORMATO VALIDO: NUMERO OPERACAO NUMERO\n\n->")
valor1, operacao, valor2 = calculo.split()
valor1 = int(valor1)
valor2 = int(valor2)


## Loop para rodar a calculadora

while operacao != "X":
    #Calcula o resultado chamando o dispatcher
    resultado = dispatcher(valor1, valor2, operacao)    
    print(f"Resultado: {resultado}\n")
    #Seguimos com o calculo no mesmo formato porém agora com RESULTADO -> RESULTADO OPERACAO RESULTADO
    novo_calculo = input(f"Digite a continuacao do calculo ou 'X' para cancelar:\n->{resultado} ")

    ##Caso seja digitado um 'X' para o loop
    if novo_calculo=="X":
        break
    #Reestabelece alguns valores como valor1 (derivado de resultado) e valor2 como int
    operacao, valor2 = novo_calculo.split()
    valor1 = resultado
    valor2 = int(valor2)

print(f"\nResultado Final: {resultado}")