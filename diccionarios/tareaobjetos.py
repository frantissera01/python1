#Enunciado:
# Crea una clase llamada "Rectangulo" que represente un rectángulo y 
# tenga los siguientes atributos:  base: la longitud de la base del rectángulo.
# altura: la altura del rectángulo. La clase debe tener los siguientes métodos:
# calcular_area(): calcula y devuelve el área del rectángulo.
# calcular_perimetro(): calcula y devuelve el perímetro del rectángulo.
#A continuación, crea una instancia de la clase Rectangulo 
# con una base = 5 y una altura= 3. 
# Luego, muestra el área y el perímetro del rectángulo utilizando los métodos de la clase.

class rectangulo :
    def __init__(self, base,altura):
        self.base=base
        self.altura=altura
    def calcular_area(self):
        return self.base*self.altura
    def calcular_perimetro(self):
        return (self.base + self.altura)*2
    
rectangulo= rectangulo(5,3)

print("los resultados son los siguientes: \n La altura del rectangulo es: ", rectangulo.altura)
print(" La base del rectangulo es: ", rectangulo.base)
print(" El area del rectangulo es: ", rectangulo.calcular_area())
print(" El perimetro del area es : ", rectangulo.calcular_perimetro())
        