sexo = str(input("Insira o sexo (utilize 'M' ou 'H'): "))
if (sexo == "M" or sexo == "H"):
    alt = float(input("Insira a altura (em metros): "))
    if (sexo == "M"):
        result = (62.1*alt)-44.7
        print("O peso ideal é: ", result, "Kg")
    else:
        result = (72.7*alt)-58
        print("O peso ideal é: ", result, "Kg")
else:
    print("Sexo inválido")