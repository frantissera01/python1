num=0
cont=0
suma=0
contP=0
contI=0
porP=0
porI=0
prom=0
while (cont<50):
    msj="ingresar numero"+str(cont+1)
    print(msj)
    num=int(input(""))
    if(num/2==0):
        contP=contP+1
        suma=suma+num
    else:
        contI=contI+1
    cont=cont+1
if(contP>0):
    prom=suma/contP
porP=contP*100/cont
porI=contI*100/cont
msj="promedio pares " +str(prom)
print(msj)
msj="porcentaje impares " +str(porI)
print(msj)
