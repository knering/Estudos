#Forma uma lista com notas, somas e médias

notas = []; soma=0; media=0;i=0;acima_media=0

while i <= 100:
    nota = float(input("Insira a nota: "))
    if nota == -1:
        break
    else:
        notas.append(nota)
        soma = soma + nota
    i +=1
media = soma/i

print("Quantidade de valores lidos: ", i)
print(notas)

while i >0:
    i -=1
    print(notas[i])

print("A soma dos valores é: ", soma)
print("A media: ", media)
print("Valores maiores que a média: ")

for n in notas:
    if n > media:
        acima_media +=1
print(acima_media)