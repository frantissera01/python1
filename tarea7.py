from random import Random


vec1=[]
vec2=[]
vec3=[]
num=0
for i in range (0,10):
    num=Random.randint(1,20)
    vec1.append(num)
    num= Random.randint(1,20)
    vec2.append(num)
for i in range(0,10):
    if (i/2==0):
     vec3.append(vec1[i]+vec2[i])
else:
    vec3.append(vec1[i]*vec2[i])
for i in range (0,10):
    if (i/2==0):
     msj=str (vec1[i])+ "+" + str(vec2[i]) + "=" + str(vec3[i])
else:
    msj=str (vec1[i])+"*"+ str (vec2[i]) + "=" + str(vec3[i])
    print (msj)
    
    