#Algoritmo que identifica o maior valor dentre as entradas do usuário

def maiorvalor(num=0, maior=None):
    while num != '':
        numero = input("Insira o numero, aperte enter para parar: ")
        if numero == '':
            break
        numero = int(numero)
        if maior == None or numero > maior:
            maior = numero
    print("O maior numero é: ", maior)

maiorvalor()