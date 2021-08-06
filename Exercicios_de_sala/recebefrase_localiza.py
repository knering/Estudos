# Algoritmo de localização de caractere em frase

j = 0
frase = input("Insira a frase: ")
letra = input("Insira a letra: ")
for i in frase.upper():
    if i == letra.upper():
        print("Letra", letra, "na posição: ", j)
    j += 1
