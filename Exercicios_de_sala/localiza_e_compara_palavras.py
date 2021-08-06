#Algoritmo que localiza e compara palavras

indice = 0;j=0; palavraespaçada=[]; arg =''; programação = "PROGRAMAÇÃO"; palavra_final=0

disciplina = input("Digite a disciplina: ")

for i in disciplina:
    if i == " ":
        indice = j
    j +=1

indice +=1

while indice < len(disciplina):
    palavraespaçada.append(disciplina[indice])
    indice += 1

palavra_final = arg.join(palavraespaçada)

if palavra_final.upper() == programação.upper():
    print("É da categoria de programação")
else:
    print("Não é da categoria de programação")