vec=[4,5,7,7,7,8,8,4,5]
cont=0
mayor=0
for i in range (0, len(vec)):
    if(i==0):
     mayor=vec[i]
    cont=1
    if(i>0):
        if(vec[i>mayor]):
            mayor=vec[i]
            cont=1
        else:
         if(vec[i]==mayor):
             cont=cont+1
msj="el mayor es " + str(mayor) + "y se repite "+ (cont)
print (msj)           
        