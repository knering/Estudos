lista = []
n = 0
soma = 0
maiores = 0
menores = 0

while True:
    print("Insira -1 para parar")
    valor = float(input("Insira a nota: "))
    if valor == -1:
        break
    lista.append(valor)
    soma = soma + valor
    n += 1

media = soma/n

print("Quantidade de valores lidos: ",n)
print("Valores lidos: ", lista)
print("Valores em ordem inversa: ")
lista.reverse()
for i in lista:
    print(i)
    if i > media:
        maiores += 1
    if i <7:
        menores += 1

print("A soma dos valores é: ", soma)
print("A média é: ", media)
print("Há",maiores,"valores acima da média e ",menores,"valores abaixo de sete")