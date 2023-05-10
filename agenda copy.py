dni=""
nombre=""
telefono=""
msj=""
vecdni=[]
vecnom=[]
vectelef=[]
opcion=0
funciones=0
Fin=False
while (Fin==False):
    msj= "1- agregar, 2- modificar, 3- eliminar, 4- imprimir, 5- salir "
    print(msj)
    opcion=int(input(""))
    if(opcion==1):
        msj= "Ingresar dni "
        print(msj)
        dni=input("")
        msj= "Ingresar Nombre "
        print(msj)
        nombre=input("")
        msj= "Ingresar telefono "
        print(msj)     
        telefono=input("")
        vecdni.append(dni)
        vecnom.append(nombre)
        vectelef.append(telefono)   
    if(opcion==4):
        funciones.imprimir(vecdni,vecnom,vectelef)
        car= input ("presionar tecla")
    if (opcion==3):
        msj= "ingresar dni a borrar "
        print (msj)
        dni= input ("")
        funciones.borrar (dni, vecdni, vecnom, vectelef)
    if (opcion==5):
        Fin=True
def imprimir(vec1, vec2, vec3):
    msj=""
    for i in range(0,len(vec1)):
        msj="dni"+str(vec1[i])
        msj=msj+"nombre"+vec2[i]
        msj=msj+"telefono"+vec3[i]
        print(msj)
        
def borrar (dni, vec1, vec2, vec3):
    msj= ""
    for i in range (0, len (vec1)):
        if(dni==vec1[i]):
            vec1.pop(i)
            vec2.pop(i)
            vec3.pop(i)