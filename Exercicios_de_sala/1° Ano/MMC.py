#Algoritmo de calculo de MMC

dividendo = 0; divisor = 0; c=0

a = int(input("Insira o primeiro numero: "))
b = int(input("Insira o segundo numero: "))

if (b > a):
    dividendo = b
    divisor = a
else:
    dividendo = a
    divisor = b

while (dividendo % divisor != 0):
    c = dividendo % divisor
    dividendo = divisor
    divisor = c

print ("O MMC é: ", divisor)
