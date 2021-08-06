#Algoritmo de eleição e contagem de votos com 4 candidatos

can_1 = 0; can_2 = 0; can_3 = 0; can_4 = 0; brancos = 0; nulos = 0; voto = 7

while (voto != 0):
    voto = int(input("Insira o seu voto: "))

    if (voto == 1 ):
        can_1 = can_1 +1
    elif (voto == 2):
        can_2 = can_2 +1
    elif (voto == 3):
        can_3 = can_3 +1
    elif (voto == 4):
        can_4 = can_4 +1
    elif (voto == 5):
        nulos = nulos +1
    elif (voto == 6):
        brancos = brancos +1

print ("Total de votos para cada candidato: ")
print (" Candidato 1: ", can_1)
print (" Candidato 2: ", can_2)
print (" Candidato 3: ", can_3)
print (" Candidato 4: ", can_4)
print ("Total de votos nulos: ", nulos)
print ("Total de votos brancos: ", brancos)