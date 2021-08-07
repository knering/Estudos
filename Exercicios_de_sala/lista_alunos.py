def ler_formatado():
    arq = open("lista_alunos.txt","r")
    for linha in arq.readlines():
        lista_linha = linha.split(",")
        media = (float(lista_linha[2]) + float(lista_linha[3]) + float(lista_linha[4]))/3
        print("Matrícula: ", lista_linha[0],"\nNome: ",lista_linha[1], "\nMédia: ",media)
        if media >= 8.5:
            print("Conceito: Excelente")
        elif 7.0 <= media < 8.5:
            print ("Conceito: Bom")
        elif 5.0 <= media < 7.0:
            print("Conceito: Regular")
        else:
            print("Conceito: Preocupante")
        print("-----------------------------------")
    arq.close()
 
def escrever_lista():
    while True:
        arq = open("lista_alunos.txt","w")
        RA = input("Insira o numero de matrícula (aperte espaço para parar):")
        if RA == " ":
            arq.close()
            ler_formatado()
            break
        else:
            nome = input("Insira o nome: ")
            nota1 = input("insira a primeira: ")
            nota2 = input("insira a segunda: ")
            nota3 = input("insira a terceira: ")
            print("---------------------")
            arq.write(RA)
            arq.write(",")
            arq.write(nome)
            arq.write(",")
            arq.write(nota1)
            arq.write(",")
            arq.write(nota2)
            arq.write(",")
            arq.write(nota3)
            arq.write("\n")
        
 
escrever_lista()
