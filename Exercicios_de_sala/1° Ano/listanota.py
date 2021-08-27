#Calculo de alunos aprovados e média

i = 0; nota1=0;nota2=0;nota3=0;nota4=0;media=0;lista = [];aprovados = 0;media_geral=0

while (i<10):
     print("----------------------------")
     nota1 = float(input("Insira a primeira nota do aluno: "))
     nota2 = float(input("Insira a segunda nota do aluno: "))
     nota3 = float(input("Insira a terceira nota do aluno: "))
     nota4 = float(input("Insira a quarta nota do aluno: "))
     media =(nota1+nota2+nota3+nota4)/4
     lista.append(media)
     if media >=7:
         aprovados +=1
     i +=1
     media_geral = (media_geral + media)/10

print ("Número de alunos com media maior ou igual a 7.0: ", aprovados)
print(" Média geral: ", media_geral)





