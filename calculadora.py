import math

def ingresa_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, ingrese un número válido.")


def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "No es posible dividir por cero."

def potencia(base, exponente):
    return base ** exponente

def radicacion(numero, indice):
    return numero ** (1 / indice)

while True:
   
    print("\n Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Radicación")
    print("7. Salir")
    
    opcion = input("Ingrese el número de la operación deseada: ")
    
    if opcion == "1":
        num1 = ingresa_numero("Ingrese el primer número: ")
        num2 = ingresa_numero("Ingrese el segundo número: ")
        resultado = suma(num1, num2)
        print("El resultado es: ", resultado)
    elif opcion == "2":
        num1 = ingresa_numero("Ingrese el primer número: ")
        num2 = ingresa_numero("Ingrese el segundo número: ")
        resultado = resta(num1, num2)
        print("El resultado es: ", resultado)
    elif opcion == "3":
        num1 = ingresa_numero("Ingrese el primer número: ")
        num2 = ingresa_numero("Ingrese el segundo número: ")
        resultado = multiplicar(num1, num2)
        print("El resultado es: ", resultado)
    elif opcion == "4":
        num1 = ingresa_numero("Ingrese el primer número: ")
        num2 = ingresa_numero("Ingrese el segundo número: ")
        resultado = dividir(num1, num2)
        print("El resultado es: ", resultado)
    elif opcion == "5":
        base = ingresa_numero("Ingrese la base: ")
        exponente = ingresa_numero("Ingrese el exponente: ")
        resultado = potencia(base, exponente)
        print("El resultado es: ", resultado)
    elif opcion == "6":
        numero = ingresa_numero("Ingrese el número: ")
        indice = ingresa_numero("Ingrese el índice de la raíz: ")
        resultado = radicacion(numero, indice)
        print("El resultado es: ", resultado)
    elif opcion == "7":
        print("Adios")
        break
    else:
        print("Opcion invalida, presiona enter para continuar. ")
