def tabuada(num):
    i=0
    while i<=10:
        mul = i*num
        print(num,"x",i," = ", mul)
        i += 1

numero = int(input("Insira um numero: "))
tabuada(numero)