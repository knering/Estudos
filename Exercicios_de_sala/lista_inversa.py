#Algoritmo que inverte uma lista

lista_original=[];lista_invertida=[];i=0

while i<5:
    lista_original.append(int(input("Insira o valor: ")))
    i +=1

while i >0:
    i -=1
    lista_invertida.append(lista_original[i])

print(lista_original)
print(lista_invertida)