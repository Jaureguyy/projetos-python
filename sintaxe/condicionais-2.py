##Ler um numero correspondente a um mes do ano, depois imprimir a estacao correspondente

mes = int(input("Mes do ano: "))

if mes==12 or mes==1 or mes==2:
    print("Verao")
elif mes==3 or mes==4 or mes==5:
    print("Outono")
elif mes==6 or mes==7 or mes==8:
    print("Inverno")
elif mes==9 or mes==10 or mes==11:
    print("Primavera")
else:
    print("Mes invalido")