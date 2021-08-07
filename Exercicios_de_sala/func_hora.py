def minutos(hrs):
    min = hrs*60
    return min

def somaMinutos(min,hrs):
    somamin = minutos(hrs) + min
    return somamin

def segundos(min,hrs):
    segundos = somaMinutos(m,h)*60
    print(segundos)

h = int(input("Insira a hora: "))
m = int(input("Insira os minutos: "))

segundos(m,h)