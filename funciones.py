def imprimir(vec1, vec2, vec3):
    msj=""
    for i in range(0,len(vec1)):
        print("--------------------------")
        msj="dni" + str(vec1[i])
        msj=msj+ "nombre" + str(vec2[i])
        msj=msj+ "telefono" + str(vec3[i])
        print(msj)
        
def borrar (dni, vec1, vec2, vec3):
    msj= ""
    b=0
    indice=0
    for i in range (0, len (vec1)):
        if(dni==vec1[i]):
            indice=ib=1
    if (b==1):
         vec1.pop(i)
         vec2.pop(i)
         vec3.pop(i)
         msj= "contacto borrado"
    else: 
        msj= "no existe dni"
        print (msj)