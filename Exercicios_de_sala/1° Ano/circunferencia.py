# Com base no raio, determina comprimento, area e volume de uma esfera

import math

r = float(input("Insira o raio da esfera: "))
comp = 2*math.pi*r
area = math.pi*pow(r,2)
vol = (3/4)*math.pi*pow(r,3)

print ("Comprimento = ", comp)
print ("Area = ", area)
print ("Volume = ", vol)