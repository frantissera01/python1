suma=0
cpar=0
prom=0
compar=0
b=0
porc=0
vec=0
for i in range (0, len(vec)):
    if(vec[i]/2==0):
        suma=suma+vec[i]
        cpar=cpar+1
    else:
        compar=compar+1
        if(b==0):
            menor=vec[i]
            b=1
        else:
         if(vec[i]<menor):
             menor=vec[i]
if(cpar>0):
    prom=suma/cpar
porc=compar*100/(cpar+compar)
msj="promedio pares" +str(prom)
print(msj)
msj="porcentaje impares"+str(porc)
print(msj) 
msj="menor de impares " + str(menor )
print(msj)

    
