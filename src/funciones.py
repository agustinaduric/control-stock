def agregar_producto(productos):
    producto_nuevo = {
        "nombre": input("Ingrese el nombre del producto: "),
        "precio": float(input("Ingrese el precio: ")),
        "cantidad": int(input("Ingrese la cantidad: "))
    }
    productos.append(producto_nuevo)