def calc_imc(altura,peso):
    indice = peso/ altura**2
    return indice

def imc(sexo="MULHER"):
    indice = calc_imc(altura,peso)
    if sexo == "MULHER":
        if indice <19.1:
            print("Abaixo do peso")
        elif indice >= 19.1 and indice <=25.8:
            print("No peso normal")
        elif indice >25.8 and indice <=27.3:
            print("Marginalmente acima do peso")
        elif indice >27.3 and indice <=31.1:
            print("Acima do peso ideal")
        elif indice > 31.1:
            print("Obeso")
    elif sexo == "HOMEM":
        if indice <20.7:
            print("Abaixo do peso")
        elif indice >= 20.7 and indice <=26.4:
            print("No peso normal")
        elif indice >26.4 and indice <=27.8:
            print("Marginalmente acima do peso")
        elif indice >27.8 and indice <=32.3:
            print("Acima do peso ideal")
        elif indice > 32.3:
            print("Obeso")

sexo = str(input("Insira o sexo: "))
peso = float(input("Insira o peso: "))
altura = float(input("Insria a altura: "))

imc(sexo)