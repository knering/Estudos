
# Seleciona entre 3 opções e mostra a média entre dois numeros, diferença e produto deles

while True:
    print("----------------------------------------------------")
    print("1 - A média entre os dois números")
    print("2 - A diferença do maior pelo menor")
    print("3 - O produto entre os dois números")
    opção = int(input("Insira a opção correspondente ao resultado desejado: "))
    if (opção != 1 and opção != 2 and opção != 3):
        print("Opção inválida")
        break
    else:
        n1 = float(input("Insira o primeiro número: "))
        n2 = float(input("Insira o segundo número: "))

        if (opção == 1):
            result = (n1+n2)/2
            print("A média é:", result)

        elif (opção ==2):
            if (n2>n1):
                maior = n2
                menor = n1
            else:
                maior = n1
                menor = n2
            result = maior - menor
            print("A diferença é:", result)

        elif (opção ==3):
            result = n1*n2
            print("O produto dos números é:", result)
