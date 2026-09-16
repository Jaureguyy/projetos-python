#O desempacotamento já era algo que eu estava utilizando sem saber, sempre que eu fazia: a, b = input(*****) ; ele estava desempacotando uma tupla
#Um exemplo é:
### tupla = ("Ana", 25, "SMO")                                                                                            
### nome, idade, cidade = tupla                    

### Caso eu de print nestas variáveis da esqureda, elas irão coincidir com os elementos da tupla. Esta propriedade também é válida para listas.
### Se na ocasião uma variável precisa ser ignorada, é possível utilizar '_' para ignorar, seguindo para a próxima.


tupla = ("Matheus", 67, "São Paulo", "Designer")
print(f"{tupla}\n")
nome, idade, estado, profissao = tupla

print(nome)
print(idade)
print(estado)
print(profissao)
print(f"\n{'-'*30}\n")

## Se a quantidade de variáveis para desempacotar a tupla for menor, irá retornar erro. Neste caso o que é possível fazer é utilizar um '*' para capturar o resto

nova_tupla = ("Guilherme", "Matheus", "Joana", "Otavio")
aluno1, aluno2, *aluno3 = nova_tupla

print(aluno1)
print(aluno2)
print(*aluno3)