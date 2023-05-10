#el usuario debe ingresar dos numeros y la maquina arrojart el mayor y menor
def maximo(a,b):
  if x>y:
    return x
  else:
    return y

 
def minimo(a,b):
  if x<y:
    return x
  else:
    return y

 
x=int(input("Un número: "))
y=int(input("Otro número: "))
resultado=(x,y) #(??????
print(resultado)

#el usuario debe ingresar un nombre que comience con C, si ingresa es valo sino invalido
def validar(nombre):
    caracterBuscado="C"
    emailValido=False
    for c in nombre:
        if c==caracterBuscado:
            return True
    return False

 
nombre=input("nombre: ")
if validar(nombre):
    print("nombre válido")
else:
    print("nombre inválido")
    
#el usuario debe ingresar numeros y el programa hara la suma. el programa termina cuando ingrese cero.
def sumaDigitos(numero):
    suma=0
    while numero!=0:
        digito=numero%10
        suma=suma+digito
        numero=numero//10
    return suma

 
num=int(input("Número a procesar: "))
while num!=0:
    print("Suma:",sumaDigitos(num))
    num=int(input("Número a procesar: "))
    
#el usuario debe ingresar un numero y el programa verifica si es primo o no.
def primo(num):
   for i in range(2,num):
       if num%i==0:           
           return False
   return True

 
numero=int(input("Número: "))
if primo(numero):
    print("Es primo")
else:
    print("No es primo")


#el usuario debe ingresar su dni, para que sea valido debe tener entre 7 y 8 digitos.
def validarDNI(dni):
   cantidad=0
   while dni!=0:
       cantidad+=1
       dni//=10
   return cantidad==7 or cantidad==8