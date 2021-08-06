#Algoritmo de calculo de média

n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insira a segunda nota: "))
media = (n1+n2)/2

if(media <= 3.9):
    print("Média: ",media, ". Você foi reprovado")
elif (media >= 4 and media <= 6.9):
    print("Média: ",media, ". Você está de exame")
else:
    print("Média: ",media, ". Você foi aprovado")
        