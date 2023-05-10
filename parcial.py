import random
import os 
from fractions import Fraction
opcion=0
valor_pendiente=0
valor_ordenada=0
pendiente=""
raiz=0

valor_pendiente= Fraction(input("Ingrese el coeficiente principal. Siendo ax + b, ingrese el valor de a\n"))

valor_ordenada=Fraction(input("Ingrese el termino independiente.Siendo ax+b,ingrese el valor de b\n"))

if(valor_pendiente>0):
    pendiente="creciente"
else:
    pendiente="decreciente"
    
raiz= (valor_ordenada*-1)/valor_pendiente

print("corte en x = " + str (raiz))
print ("corte en x = " + str (valor_ordenada))
print("pendiente = " + str(pendiente))


