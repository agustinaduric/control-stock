from src.db import conectar

def buscar_producto(campo, valor):
    conexion = conectar()
    cursor = conexion.cursor()

    query = f"SELECT * FROM productos WHERE {campo} LIKE ?;"
    cursor.execute(query, (f"%{valor}%",))
    productos = cursor.fetchall()
    conexion.close()

    if not productos:
        print("\nNo se han encontrado productos.")
    else:
        print("\nResultados de la búsqueda:")
        print("ID".ljust(5) + "Nombre".ljust(20) + "Precio".ljust(10) + "Cantidad".ljust(10) + "Descripcion".ljust(20) + "Categoria")
        for producto in productos:
            print(f" {str(producto[0]).ljust(5)}{producto[1].ljust(20)} {str(producto[2]).ljust(10)} {str(producto[3]).ljust(10)} {producto[4].ljust(20)} {producto[5]}")