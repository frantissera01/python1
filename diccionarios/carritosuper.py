from decimal import Decimal

#perro

productos = {
    "01": {
        "Nombre": "Iphone 6",
        "Codigo": "01",
        "Marca": "Apple",
        "Precio": 150.25,
        "Stock": 10,
        "Color": "Blanco",
        "Caracteristica": "16gb",
    },
    "02": {
        "Nombre": "Iphone 7",
        "Codigo": "02",
        "Marca": "Apple",
        "Precio": 204.99,
        "Stock": 5,
        "Color": "Negro",
        "Caracteristica": "64gb",
    },
    "03": {
        "Nombre": "Iphone 8",
        "Codigo": "03",
        "Marca": "Apple",
        "Precio": 240,
        "Stock": 8,
        "Color": "Rojo",
        "Caracteristica": "32gb",
    },
    "04": {
        "Nombre": "Iphone X",
        "Codigo": "04",
        "Marca": "Apple",
        "Precio": 282.50,
        "Stock": 3,
        "Color": "Blanco",
        "Caracteristica": "132gb",
    },
    "05": {
        "Nombre": "Iphone 11",
        "Codigo": "05",
        "Marca": "Apple",
        "Precio": 299.99,
        "Stock": 2,
        "Color": "Negro Mate",
        "Caracteristica": "256gb ",
    },
}

stock = {
    "01": {
        "Nombre": "Iphone 6",
        "Stock": 10
    },
    "02": {
        "Nombre": "Iphone 7",
        "Stock": 5
    },
    "03": {
        "Nombre": "Iphone 8",
        "Stock": 8
    },
    "04":{
        "Nombre": "Iphone X",
        "Stock": 3
    },
    "05": {
        "Nombre": "Iphone 11",
        "Stock": 2
    }
}


carrito = {}


def mostrar_producto_detalle():
    print("==== DETALLES DE PRODUCTOS ====")
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
    codigo = input("Ingrese el código del producto: ")
    if codigo in productos:
        producto = productos[codigo]
        print("==== DETALLES DEL PRODUCTO ====")
        print("Código: ", codigo)
        print("Nombre: ", producto["Nombre"])
        print("Precio: ", producto["Precio"])
        print("-----------------------------")
        
    else:
        print("Producto no encontrado.")

def realizar_compra():
    codigo = input("Ingrese el código del producto: ")
    if codigo in productos:
        producto = productos[codigo]
        stock = int(input("Ingrese la cantidad a comprar: "))
        if stock > producto["Stock"]:
            print("No hay suficiente stock disponible.")
            print("Ingrese nuevamente la cantidad deseada. ")
        else:
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
            print("Producto agregado al carrito de compras.")
    else:
        print("Producto no encontrado.")

def finalizar_compra():
    if not carrito:
        print("No hay productos agregados al carrito.")
        return

    print("==== DETALLES DE LA COMPRA ====")
    total_compra = 0
    for codigo, item in carrito.items():
        nombre_producto = item["Nombre"]
        cantidad = item["Stock"]
        precio_unitario = item["Precio unitario"]
        costo_total = item["Costo total"]
        total_compra += costo_total
        print("Producto: ", nombre_producto)
        print("Stock ", stock)
        print("Precio unitario: ", precio_unitario)
        print("Costo total: ", costo_total)
        print("-----------------------------")

    print("Total de la compra:", total_compra)
    stock[codigo]["Stock"] += cantidad



def visualizar_carrito():
    print("==== PRODUCTOS EN EL CARRITO ====")
    for codigo, item in carrito.items():
        nombre_producto = item["Nombre"]
        stock = item["Stock"]
        precio_unitario = item["Precio unitario"]
        costo_total = item["Costo total"]
        print("Código:", codigo)
        print("Nombre:", nombre_producto)
        print("Cantidad:", stock)
        print("Precio unitario:", precio_unitario)
        print("Costo total:", costo_total)
        print("-----------------------------")

def modificar_carrito():
    visualizar_carrito()
    codigo = input("Ingrese el código del producto que desea modificar: ")
    if codigo in carrito:
        producto = carrito[codigo]
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
        if nueva_cantidad > 0:
            producto["Stock"] = nueva_cantidad
            producto["Costo total"] = producto["Precio unitario"] * nueva_cantidad
            print("Cantidad modificada correctamente.")
        else:
            del carrito[codigo]
            print("Producto eliminado del carrito.")
    else:
        print("Producto no encontrado en el carrito.")
        
def mostrar_productos_disponibles():
    print("==== PRODUCTOS DISPONIBLES ====")
    for codigo, producto in stock.items():
        print("Nombre: ", producto["Nombre"])
        print("Codigo: ", codigo)
        print("Cantidad disponible:", producto["Stock"])
        print("-----------------------------")
        


carrito = {}




def menu_principal():
    while True:
        print("--Bienvenido a SmartApple--")
        mostrar_productos_disponibles()
        print("==== MENÚ ====")
        print("1. Mostrar producto en detalle")
        print("2. Buscar producto por código")
        print("3. Realizar compra")
        print("4. Finalizar compra")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_producto_detalle()
        elif opcion == "2":
            buscar_producto_por_codigo()
        elif opcion == "3":
            realizar_compra()
        elif opcion == "4":
            if not carrito:
                print("No hay productos agregados al carrito.")
            else:
                while True: 
                    print("---Antes de finalizar, ¿Desea modificar su compra?---")
                    opcion_finalizar = mostrar_menu_finalizar()
                    if opcion_finalizar == "1":
                        finalizar_compra()
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
            print("La opcion ingresada es invalida. Ingrese de nuevo la opcion deseada ")

def mostrar_menu_finalizar():
    print("1. Finalizar compra")
    print("2. Visualizar carrito")
    print("3. Modificar carrito")
    print("4. Volver atrás")
    opcion = input("Ingrese su opción: ")
    return opcion

menu_principal()

