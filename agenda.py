import funciones
import os

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
    os.system("cls")
    msj= "1- agregar, 2- modificar, 3- eliminar, 4- imprimir, 5- salir "
    print(msj)
    opcion=int(input(""))
    if(opcion==1):
        msj= "Ingresar dni "
        print(msj)
        dni=int(input(""))
        msj= "Ingresar Nombre "
        print(msj)
        nombre=str(input(""))
        msj= "Ingresar telefono "
        print(msj)     
        telefono=int(input(""))
        vecdni.append(dni)
        vecnom.append(nombre)
        vectelef.append(telefono)  
    if (opcion==3):
        msj= "ingresar dni a borrar "
        print (msj)
        dni= input ("")
        funciones.borrar(dni, vecdni, vecnom, vectelef) 
    if(opcion==4):
        funciones.imprimir(vecdni, vecnom, vectelef)
        car= input ("presionar tecla")
    if (opcion==5):
        Fin=True

