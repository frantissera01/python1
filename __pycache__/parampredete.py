#quiere imprimir una lista con ejercicios de gym
def gimnasio(ejercicio= "seguir", noejercicio="no hay ejercicio"):
    listagym=[]
    while(ejercicio== "seguir"):
        ejercicio=input("sigue algun ejercicio?")
        if(ejercicio=="seguir"):
            noejercicio=(input("ingrese un ejercicio:    "))
            listagym.append(ejercicio)
    return listagym

print(gimnasio())

#debe imprimir el siguiente calculo 
def calculo(num1=7, num2=4, num3=9):
    return ((num1 + num2) - num3)
print(calculo())

#debe realizar la suguiente multiplicacion
def multiplica(numA=4):
    return(numA * numA)
print(multiplica())


#quiero que me imprima la fecha de hoy en caso de no ser la correcta, imprima error
def fecha(hoy="error"):
    print("hoy es:  " + hoy)

fecha("15/05/2023")

#quiero que la funcion me imprima dia y hora 
def fechahora(orden1="15/05", orden2="22.58"):
    print(f"hoy es {orden1} y el horario es {orden2}")
    
fechahora("15/05", "22.58")