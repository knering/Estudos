i = 1; media_maior = 0; media_menor = 100; aprovados = 0; reprovados = 0; media_geral = 0

while (i<=2):
    print("-----------------------------------------------")
    print("Aluno ",i)
    matricula = int(input("Insira o numero de matricula: "))
    freq = int(input("Insira a frequência (em %): ")) 
    ##inserindo dessa forma a variavel pois o enunciado do exercicio não é conclusivo sobre quantas aulas foram dadas, nao permitindo calcular a frequência.
    nota1 = float(input("Insira a primeira nota: "))
    nota2 = float(input("Insira a segunda nota: "))
    nota3 = float(input("Insira a terceira nota: "))

    media = (nota1+nota2+nota3)/3
    if (media > media_maior):
        media_maior = media
    elif (media < media_menor):
        media_menor = media
    
    media_geral = (media_geral + media)/i
    i +=1

    if (media >= 6 and freq >= 75):
        print ("O aluno de matrícula ", matricula, ", com a frequência de", freq"%", ",está aprovado e possui média de", media)
        aprovados +=1
    else:
        print ("O aluno de matrícula ", matricula, ", com a frequência de", freq"%", ",está reprovado e possui média de", media)
        reprovados +=1

print("------------------------------------")
print("A maior média da turma é de: ", media_maior)
print("A menor média da turma é de: ", media_menor)
print("A média geral da turma é de: ", media_geral)
print(aprovados, "alunos estão aprovados")
print(reprovados, "alunos estão reprovados")
