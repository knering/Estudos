#Calcula somatório e média por valores inseridos

entrada = 1
somatorio = 0
media = 0
i = 0

while True:
    entrada = float(input("Insira o valor desejado: "))
    if (entrada <=0):
        break
    else:
        i +=1
        somatorio = somatorio + entrada
        media = somatorio/i
    

print ("O somatório dos números é: ", somatorio)
print ("A média dos números é: ", media)