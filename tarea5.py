import random


vec=[]
vec1=[]
vec2=[]
num1=0
num2=0
for i in range (0, 10):
    num1=random.randint(1,11)
    num2=random.randint(1,11)
    vec.append(num1)
    vec1.append(num2)
    vec2.append (num1 x num2)
for i in range (0,10):
    msj=str(vec[i]) + "x" + str(vec1[i]) + "=" + str (vec2[i])
print (msj)