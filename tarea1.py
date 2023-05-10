suma=0
cont=0
num=0
prom=0
msj=""
while (cont<10):
  print("ingresar numero")
  num=int(input(""))
  suma=suma+num
  cont=cont+1
prom=suma/cont
msj="el promedio es " + str (prom)
print(msj)