def registrar_producto(productos):
    print("Alta de Producto")
    producto_nuevo = {
        "id": int(input("ID: ")),
        "nombre": input("Nombre: "),
        "precio": float(input("Precio: ")),
        "cantidad": int(input("Cantidad: "))
    }
    productos.append(producto_nuevo)

def registrar_producto(productos):
    print("Alta de Producto")
    producto_nuevo = {
        "id": int(input("ID: ")),
        "nombre": input("Nombre: "),
        "precio": float(input("Precio: ")),
        "cantidad": int(input("Cantidad: "))
    }
    productos.append(producto_nuevo)


def actualizar_producto(productos):
    id = int(input("ID del producto a modificar: "))
    encontrada = False
    for prod in productos:
        if id == prod["id"]:
            nueva_cantidad = int(input(f"Nueva cantidad (Actual --> {prod['cantidad']}): "))
            prod["cantidad"] = nueva_cantidad
            print("Producto Actualizado")
            encontrada = True
            break
    if not encontrada:
        print(f"El producto con id: {id} no existe en el listado actual")


def eliminar_producto(productos):
    id = int(input("ID del producto a eliminar: "))
    encontrada = False
    for prod in productos:
        if id == prod["id"]:
            productos.remove(prod)
            print("Producto Eliminado !!!")
            encontrada = True
            break
    if not encontrada:
        print(f"El producto con id: {id} no existe en el listado actual")


def mostrar_productos(productos):
    print("Listado")
    if len(productos) == 0:
        print("Aun no tenemos productos cargados en el sistema")
    else:
        print("ID".ljust(5) + "Nombre".ljust(30) + "Precio".ljust(10) + "Cantidad")
        for producto in productos:
            print(f"{str(producto['id']).ljust(5)}{producto['nombre'].ljust(30)}{str(producto['precio']).ljust(10)}{producto['cantidad']}")


def reporte_bajo_stock(productos):
    limite = int(input("Limite para bajo stock: "))
    if len(productos) == 0:
        print("Aun no tenemos productos cargados en el sistema")
    else:
        print("Productos con stock menor igual a " + str(limite) )
        print("ID".ljust(5) + "Nombre".ljust(30) + "Precio".ljust(10) + "Cantidad")
        for producto in productos:
            if producto["cantidad"] <= limite:
                print(f"{str(producto['id']).ljust(5)}{producto['nombre'].ljust(30)}{str(producto['precio']).ljust(10)}{producto['cantidad']}")