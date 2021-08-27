i=0; lista_int=[];n_del=0;n=0; deletado= False

while i<10:
    n = int(input("Insira um valor inteiro: "))
    lista_int.append(n)
    i +=1

n_del = int(input("Insira um valor para ser deletado: "))
i=0

while i < len(lista_int):
    if lista_int[i] == n_del:
        lista_int.remove(n_del)
        deletado = True
        i = 0
    i +=1

if deletado == False:
    print("Não há esse valor na lista!")