from random import random


cont=0
cont2=0
cont3=0
cont4=0
pr3=0
pr13=0
pr15=0
num=0
while(cont<100):
    num=random.randit(1,6)
    if(num==3):
        cont2=cont2+1
    if(num<4):
        cont3=cont3+1
    if(num<6):
        con4=cont4+1
    cont=cont+1
pr3=cont2/cont
pr13=cont3/cont
pr15=cont4/cont
msj="prob 3 " +str(pr3)
print(msj)
msj="prob 1-3 " +str(pr13)
print(msj)
msj="prob 1-4 " +str(pr15)
print(msj)

    