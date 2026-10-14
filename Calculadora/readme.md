# Calculadora

## Funcionamento 
A Calculadora possui o arquivo **operacoes.py** que possui as funções de cada operação e também o dispatcher. 
Dentro da **main.py** acontece o import apenas do '*dispatcher*'

### Dispatcher
Com as funções de cada operação feitas, elas são colocadas dentro de um '**dispacther**', que têm como parâmetros: *valor1*, *valor2* e *simbolo* (representa a operação).
 
 Dentro do dispatcher, existe um dicionário '**operacoes**', suas chaves são os símbolos de cada operação (vem como argumento) e valores as funções de operações criadas antes do dispatcher.
 
 Após o dicionário a variável **operacao** utiliza um *.get(simbolo,invalida)* para definir a operação que erá utilizada. Ao final ocorre um *return operacao(valor1,valor2).

 ### Dentro da Main

 Ao iniciar o programa, os seguintes passos acontecem:

 - Recebe uma variável **calculo**, que posteriormente é '*desempacotada*' em -> **valor1* / **operacao** / **valor2
 - Chama o dispatcher através da variável **resultado** dentro de um loop (while) -> *resultado = dispatcher(valor1,valor2,operacao)*
 - Print do resultado
 - Utiliza a variável **novo_calculo** para continuar. A diferença é que agora *valor1* sempre será o resultado da operação anterior, ou seja, a conta sempre continua a partir do resultado.
 - **novo_calculo** precisa receber 2 variáveis, primeiro o símbolo da nova operação e depois o **valor2** para ser usado como argumento. Desta maneira:

 ```python
 operacao, valor2 = novo_calculo.split()
 valor1 = resultado
 valor2 = int(valor2)
```
 - Para encerrar o loop -> *novo_calculo* == *'X'* ; Caso seja feito, será mostrado o resultado final.
 - O loop segue sempre 'acumulando' a variável **resultado** (que depois é transformada em **valor1**) dependendo da operação.

 ## Ideias Futuras

 - Interface visual 
 - Colocar a opção de seguir dentro do loop porém resetar a variável **valor1** (assim esquece o valor de *resultado*)
 - Novas operações (porcentagem, potência, raiz...)
 