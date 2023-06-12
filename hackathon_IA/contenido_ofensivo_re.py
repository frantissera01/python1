import re

lista_contenido_malicioso = ["gordo", "gorda", "perra","maricon","negro","puta","zorra","pelotudo","gorreado","idiota","gata","chorra","bulimica","anorexico"]

contenido = input("Ingrese mensaje ofensivo: ")

contenido_ofensivo = []

for palabra in lista_contenido_malicioso:
    if re.search(r'\b' + palabra + r'\b', contenido, re.IGNORECASE):
        contenido_ofensivo.append(palabra)
print("Se encontraron las siguientes palabras ofensivas en su texto: ", contenido_ofensivo)
# Realiza la acción correspondiente, como eliminar o marcar el contenido.






