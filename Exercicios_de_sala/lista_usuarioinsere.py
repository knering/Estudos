##Forma uma lista e imprime quantos par e quantos impar


lista=[]; par=0; impar =0;i=0

tamanho = int(input("Insira a quantidade de valores que deseja inserir: "))

while i < tamanho:
    lista.append(int(input("Insira um valor na lista: ")))
    i +=1

for j in lista:
    if j%2 == 0:
        par +=1
    else:
        impar +=1

print("Quantidade de numeros par: ",par)
print("Quantidade de numeros impar: ",impar)
