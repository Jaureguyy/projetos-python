#Ler o nome, idade e a cidade em que uma pessoa mora (três inputs). Após isso guardar os valores em uma única tupla, mostrá-la por completo e depois cada um dos elementos de forma separada

nome = input("Digite o nome de uma pessoa: ")
idade = int(input("Digite a idade da pessoa: "))
cidade = input("Digite o nome em que a pessoa mora: ")

tupla = (nome, idade, cidade)
print(f"Tupla final: {tupla}\n")

print(f"O nome da pessoa eh: {tupla[0]}")
print(f"A idade da pessoa eh: {tupla[1]}")
print(f"A cidade em que a pessoa mora eh: {tupla[2]}")