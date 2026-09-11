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

