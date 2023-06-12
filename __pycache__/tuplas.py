#lista termos 

listatermos=[("termo",2100,4,"stanley"),("termoverde",1700,3,"patopampa"),("termoazul",2100,6,"stanley")]
marca="patopampa"
preciomax=2000
lista1=[]
for c in listatermos:
    if c[1]>=preciomax and c[3]==marca:
        lista1.append(c)
        
print(lista1)


##lista chocolates 
listachocolates= [("chocoamargo", 500, 9, "arcor"), ("chocoblanco", 600, 8, "milka"), ("chocolatesnegro", 400, 5, "coofler")]
preciomaximo=700
marca="arcor"
stock=3
lista2=[]
for t in listachocolates:
    if (t[1]<=preciomaximo) and (t[3]==marca) and (t[2]==stock):
        lista2.append(t)
    else:
        print("no hay elementos en la lista")
print(lista2)


























