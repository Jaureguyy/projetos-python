#Argumentos nomeados:
#Quando utilizados a ordem de apresentação é dispensada:

#  def funcao(nome, idade)
# funcao(idade=100, nome="Joel")        argumentos nomeados fazem com que a ordem deixe de importar

#Utilizar uma função de exponencial e apresentá-la de 3 maneiras: posicional, nomeada (ordem invertida) e misturando base->posicional e expoente->nomeado


def potencia(base, expoente):
    valor=base
    for i in range(expoente-1):
        valor*=base
    return valor

#Utilizando base=3 ; expoente=4:

print("Funcao chamada de maneira posicional:")
print(potencia(3,4))

print(f"\nFuncao chamada de maneira nomeada:\n{potencia(expoente=4,base=3)}")
print(f"\nFuncao chamada de forma misturada:\n{potencia(3,expoente=4)}")