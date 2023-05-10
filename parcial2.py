import random
import os 
from fractions import Fraction
from math import sqrt
opcion=0
valor_pendiente=0
valor_lineal=0
valor_ordenada=0
pendiente=""
raiz=0
delta=0
tiporaiz=""
raices=0
verticex=0
verticey=0
intervalo=0
infinito=0 
intervalo_decrecimiento=0
delta=0
intervalo_crecimiento=0

valor_pendiente=Fraction(input("ingrese el coheficiente principal. Siendo ax2 + bx + c ingrese el valor de a\n "))
valor_lineal=Fraction(input("ingrese el termino lineal. Siendo ax2 + bx + c ingrese el valor de b\n"))
valor_ordenada=Fraction(input("ingrese el termino independiente. Siendo ax2 + bx + c ingrese el valor de c\n"))

if(valor_pendiente>0):
    pendiente="concava para arriba "
else:
    pendiente="concava para abajo"
   
delta=sqrt(valor_lineal*2 - 4 * valor_pendiente * valor_ordenada)

raiz=((valor_lineal*(-1)) + delta) /(2*valor_pendiente)

raices.append(raiz) 

raiz=((valor_lineal*(-1))-delta)/(2*valor_pendiente)

raices.append(raiz)

if(delta<0):
    tiporaiz=1
elif(delta==0):
    tiporaiz=2
elif(delta>0):
    tiporaiz=3

verticex= (valor_lineal *-1) /(2*valor_pendiente)

verticey=valor_pendiente+verticex**2+valor_lineal+verticex+valor_ordenada

if(pendiente==1):
    intervalo_decrecimiento ="(-infinito, " +str(verticex)+")"
    intervalo_crecimiento= "(" +str(verticex)+",+infinito)"
    print("el intervalo de decrecimiento es "+ intervalo_decrecimiento)
    print("el intervalo de crecimiento es "+ intervalo_crecimiento)
elif(pendiente==-1):
    intervalo_crecimiento="(-infinito, "+str(verticex) + ")"
    intervalo_decrecimiento= "("+ str(verticex) + ",+infinito)"
    print("el intervalo de creciemiento es " + intervalo_crecimiento)
    print("el intervalo de decrecimiento es " +intervalo_decrecimiento)
                

