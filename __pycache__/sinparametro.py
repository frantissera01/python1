#quiero que el programa me imprima una bienvenida 
def bienvenida():
    print("bienvenido al programa ")
bienvenida()

#quiero que el programa me imprima promedio de numeros pares 
import random
def prom():
    cont=0
    suma=0
    prom=0
    lista=[]
    while (cont<2):
        num= random.randint(1,36)
        lista.append(num)
        cont=cont + 1
        if(num/2==0):
            cont=cont+1
            suma=suma+num
    if(cont>0):
        prom=suma/cont
    msj="promedio pares " +str(prom)
    print(msj)
prom()

