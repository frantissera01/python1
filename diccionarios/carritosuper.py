from decimal import Decimal


productos = {
    "01": {
        "Nombre": "Iphone 6",
        "Codigo": "01",
        "Marca": "Apple",
        "Precio": 150.25,
        "Stock": 10,
        "Color": "Blanco",
        "Caracteristica": "18gb",
    },
    "02": {
        "Nombre": "Iphone 7",
        "Codigo": "02",
        "Marca": "Apple",
        "Precio": 204.99,
        "Stock": 5,
        "Color": "Negro",
        "Caracteristica": "65gb",
    },
    "03": {
        "Nombre": "Iphone 8",
        "Codigo": "03",
        "Marca": "Apple",
        "Precio": 240,
        "Stock": 8,
        "Color": "Rojo",
        "Caracteristica": "33gb",
    },
    "04": {
        "Nombre": "Iphone X",
        "Codigo": "04",
        "Marca": "Apple",
        "Precio": 282.50,
        "Stock": 3,
        "Color": "Blanco",
        "Caracteristica": "134gb",
    },
    "05": {
        "Nombre": "Iphone 11",
        "Codigo": "05",
        "Marca": "Apple",
        "Precio": 299.99,
        "Stock": 2,
        "Color": "Negro Mate",
        "Caracteristica": "257gb ",
    },
}



carrito = {}


def mostrar_producto_detalle():
    print(" \n==== DETALLES DE  LOS PRODUCTOS ====")
    for codigo, producto in productos.items():
        print("Codigo: ", codigo)
        print("Nombre: ", producto["Nombre"])
        print("Marca: ",  producto["Marca"])
        print("Precio: ", producto["Precio"])
        print("Color: ", producto["Color"])
        print("Stock: ", producto["Stock"])
        print("Caracteristica: ", producto["Caracteristica"])
        print("-----------------------------")

def buscar_producto_por_codigo():
    codigo = input("\nIngrese el código del producto: ")
    if codigo in productos:
        producto = productos[codigo]
        print("\n==== DETALLES DEL LOS PRODUCTO ====")
        print("Código: ", codigo)
        print("Nombre: ", producto["Nombre"])
        print("Precio: ", producto["Precio"])
        print("Color: ", producto["Color"])
        print("Stock: ", producto["Stock"])
        print("Caracteristica: ", producto["Caracteristica"])
        print("-----------------------------")
        
    else:
        print("Producto no encontrado.")

def realizar_compra():
    codigo = input("\nIngrese el código del producto: ")
    if codigo in productos:
        producto = productos[codigo]
        while True:
            try:
                stock = int(input("Ingrese la cantidad a comprar: "))
                if stock > producto["Stock"]:
                    print("\nNo hay suficiente stock disponible.")
                    print("Ingrese nuevamente la cantidad que deseada.")
                else:
                    break
            except ValueError:
                print("\nCantidad inválida. Ingrese un número entero.")

        nombre_producto = producto["Nombre"]
        precio_unitario = producto["Precio"]
        costo_total = precio_unitario * stock
        carrito[codigo] = {
            "Nombre": nombre_producto,
            "Stock": stock,
            "Precio unitario": precio_unitario,
            "Costo total": costo_total
        }
        producto["Stock"] -= stock 
        print("\nProducto agregado al carrito.")
    else:
        print("\nNo se encontro el producto.")


  
def finalizar_compra():
    if not carrito:
        print("\nNo se han agregado productos al carrito.")
        return

    print("\n==== DETALLES DE COMPRA ====")
    total_compra = 0
    for codigo, item in carrito.items():
        nombre_producto = item["Nombre"]
        cantidad = item["Stock"]
        precio_unitario = item["Precio unitario"]
        costo_total = item["Costo total"]
        total_compra += costo_total
        print("Producto: ", nombre_producto)
        print("Cantidad: ", cantidad)
        print("Precio unitario: ", precio_unitario)
        print("Costo total: ", costo_total)
        print("-----------------------------")
        
    print("\nTotal de la compra:", total_compra)
        


def visualizar_carrito():
    print("\n==== PRODUCTOS DENTRO DEL CARRITO ===")
    for codigo, item in carrito.items():
        nombre_producto = item["Nombre"]
        stock = item["Stock"]
        precio_unitario = item["Precio unitario"]
        costo_total = item["Costo total"]
        print("Código:", codigo)
        print("Nombre:", nombre_producto)
        print("Stock: ", stock)
        print("Precio unitario:", precio_unitario)
        print("Costo total:", costo_total)
        print("-----------------------------")

def modificar_carrito():
    visualizar_carrito()
    codigo = input("\nIngrese el código del producto que desea modificar: ")
    if codigo in carrito:
        producto = carrito[codigo]
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
        if nueva_cantidad > 0:
            producto["Stock"] = nueva_cantidad
            producto["Costo total"] = producto["Precio unitario"] * nueva_cantidad
            print("\nCantidad modificada correctamente. ")
        else:
            del carrito[codigo]
            print("\nProducto eliminado del carrito. ")
    else:
        print("\n Producto no encontrado en el carrito. ")
        
def mostrar_productos_disponibles():
    print("\n==== STOCK DISPONIBLE ====")
    for codigo, producto in productos.items():
        print("Nombre: ", producto["Nombre"])
        print("Codigo: ", codigo)
        print("Cantidad disponible:", producto["Stock"])
        print("-----------------------------")
        


carrito = {}




def menu_principal(bandera=True):
    while True:
        if bandera:
            print("\n---BIENVENIDOS A SMARTAPPLE---")
            mostrar_productos_disponibles()
        bandera = False
        print("\n==== _MENÚ_ ====")
        print("1. Mostrar los producto en detalle")
        print("2. Buscar un producto por código")
        print("3. Realizar compra")
        print("4. Finalizar compra")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            mostrar_producto_detalle()
        elif opcion == "2":
            buscar_producto_por_codigo()
        elif opcion == "3":
            realizar_compra()
        elif opcion == "4":
            if not carrito:
                print("No hay productos en el carrito.")
            else:
                while True: 
                    print("\n---Antes de finalizar, ¿Desea modificar el carrito ?---")
                    opcion_finalizar = menu_finalizar()
                    if opcion_finalizar == "1":
                        finalizar_compra()
                        bandera = True
                        break
                    elif opcion_finalizar == "2":
                        visualizar_carrito()
                    elif opcion_finalizar == "3":
                        modificar_carrito()
                    elif opcion_finalizar == "4":
                        break
                    else:
                        print("Opción inválida. Intente nuevamente.")
                        break
        elif opcion == "5":
            print("¡Muchas gracias por visitarnos! ")
            break
        else:
            print("La opcion ingresada es invalida. Ingrese de nuevo la opcion deseada. ")

def menu_finalizar():
    print("1. Finalizar la compra")
    print("2. Visualizar el carrito")
    print("3. Modificar el carrito")
    print("4. Volver atrás")
    opcion = input("Ingrese su opción: ")
    return opcion

menu_principal()

