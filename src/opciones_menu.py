from src.db import *
from src.busqueda import buscar_producto
from src.menu import menu_busqueda

def registrar_producto():
    print("\nAlta de Producto")
    print("*" * 23)
    while True:
        try:
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            descripcion = input("Descripcion: ")
            categoria = input("Categoria: ") or "General"

            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute(
                """
                INSERT INTO productos (nombre, precio, cantidad, descripcion, categoria)
                VALUES (?, ?, ?, ?, ?);
                """,
                (nombre, precio, cantidad, descripcion, categoria),
            )
            conexion.commit()
            print(f"\n'{nombre}' se ha agregado exitosamente.")
            break
        
        except sqlite3.IntegrityError:
            print("\nError: El producto ya se encuentra registrado. Intente nuevamente.")
            
        finally:
            conexion.close()
            
def buscar_producto_menu():
    menu_busqueda()
    opcion = int(input("\nSeleccione una opcion: "))

    if opcion == 1:
        id = input("\nIngrese el ID del producto: ")
        buscar_producto("id", id)
    elif opcion == 2:
        nombre = input("\nIngrese el nombre del producto: ")
        buscar_producto("nombre", nombre)
    elif opcion == 3:
        categoria = input("\nIngrese la categoria del producto: ")
        buscar_producto("categoria", categoria)
    else:
        print("\nIngrese una opcion válida.")
                  
def actualizar_producto():
    id = int(input("\nID del producto a modificar: "))
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?;", (id,))
    producto = cursor.fetchone()

    if producto:
        print(f"\nCantidad actual de {producto[1]}: {producto[3]}")
        nueva_cantidad = int(input("Nueva cantidad: "))
        cursor.execute(
            "UPDATE productos SET cantidad = ? WHERE id = ?;", (nueva_cantidad, id)
        )
        conexion.commit()
        print("\nProducto se ha actualizado correctamente.")
    else:
        print(f"\nEl producto con ID {id} no existe.")
    conexion.close()

def eliminar_producto():
    id = int(input("\nID del producto a eliminar: "))
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?;", (id,))
    producto = cursor.fetchone()

    if producto:
        cursor.execute("DELETE FROM productos WHERE id = ?;", (id,))
        conexion.commit()
        print(f"\n{producto[1]} se ha eliminado correctamente.")
    else:
        print(f"\nEl producto con ID {id} no existe.")
    conexion.close()

def mostrar_productos():
    print("\nListado de Productos")
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos;")
    productos = cursor.fetchall()
    conexion.close()

    if not productos:
        print("\nNo hay productos registrados.")
    else:
        print("\nID".ljust(5) + "Nombre".ljust(20) + "Precio".ljust(10) + "Cantidad".ljust(10) + "Descripción".ljust(20) + "Categoría")
        for producto in productos:
            print(
                f"{str(producto[0]).ljust(5)}{producto[1].ljust(20)}{str(producto[2]).ljust(10)}{str(producto[3]).ljust(10)}{producto[4].ljust(20)}{producto[5]}"
            )

def reporte_bajo_stock():
    limite = int(input("\nIngrese el limite de stock: "))

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?;", (limite,))
    productos = cursor.fetchall()
    conexion.close()

    if not productos:
        print("\nNo hay productos con bajo stock.")
    else:
        print("\nProductos con bajo stock:")
        print("\nID".ljust(5) + "Nombre".ljust(20) + "Cantidad".ljust(10))
        for producto in productos:
            print(f"{str(producto[0]).ljust(5)}{producto[1].ljust(20)}{str(producto[3]).ljust(10)}")