##ejercicio 1. Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la
##longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de
##error.
#El programa termina cuando el usuario introduce un cero.
listameses=("","enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre ")
num=1

while num !=0:
    num= int(input("ingrese un numero:  "))
    if num>12:
        print("error ")
    for i in listameses:
        if listameses.index(i)==num:
            print(i)
print("fin del programa ")


##ejercicio 2. crea una tupla con numeros, pide al usuario un numero por teclado e indica cuantas veces se 
##repite segun lo halle en la tupla que has creado.
##Resuelve validar los ingresos del usuario

tuplanum=(1,6,8,13,55,44,77,5,3,2,7,8,4,2,1,1,8,9,5,3)
num=int(input("ingrese un numero "))
print(" el numero se repite " + str(tuplanum.count(num)) + " veces")


##Ejercicio 3. crea una tupla con numeros e indica el numero con mayor valor y el que menor tenga 

tuplanum=[2,3,4,8,7,5,6,9,2,45,6,1,8,6]
numay=0
nummen=0
for i in range(0,len(tuplanum)):
    if(i==0):
        numay=tuplanum[i]
        nummen=tuplanum[i]
    if(tuplanum[i]>numay):
        numay=tuplanum[i]
    if(tuplanum[i]<nummen):
        nummen=tuplanum[i]
print("el numero mayor es  " + str (numay) + "el numero menor es  " + str (nummen))

##Ejercicio 4. crea una tupla con valores predeterminados del 1 al 10, pide al usuario un indice por 
##teclado y muestra los valores de la tupla.
#Resuelve el caso en que no exista ese indice en la tupla

tupla1al10=[1,2,3,4,5,6,7,8,9,10]
num=int(input("ingrese le numero de indice "))
print(tupla1al10 [num])