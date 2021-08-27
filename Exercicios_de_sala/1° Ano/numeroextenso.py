#Algoritmo que printa o numero inserido de forma extensa

numeros = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]; numero_extenso =[]; i=0

num = str(input("Insira o numero: "))

for i in num:
    numero_extenso.append(numeros[int(i)])

print(numero_extenso)