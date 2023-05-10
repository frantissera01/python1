vecnom=[]
vecnot1=[]
vecnot2=[]
nombres=""
nota1=0
nota2=0
promedio=0
mayprom=0
nommayprom=""
for i in range (0,20):
    print ("ingresar nombre")
    nombre=input("")
    print("ingresar nota 1 ")
    nota1= input("")
    print ("ingresar nota 2")
    nota2=input ("")
    vecnom.append(nombre)
    vecnot1.append(nota1)
    vecnot2.append(nota2)
for i in range (0,20):
    promedio(vecnot1[i] + vecnot2[i]/2)
    if(i==0):
     mayprom=promedio
     nommayprom=vecnom[i]
    if(promedio>mayprom):
     mayprom=promedio
     nommayprom=vecnom[i]
msj="alumno mayor promedio" + nommayprom + str (mayprom)
print(msj)
