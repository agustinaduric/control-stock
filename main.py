from src import funciones

productos = []

while True:
    print("\nMenu de gestion de stock")
    print("\t1. Agregar producto")
    print("\t2. Consultar datos de un producto")
    print("\t3. Modificar cantidad de stock")
    print("\t4. Mostrar todos los productos")
    print("\t5. Salir")

    opcion = int(input("\nSelecione una opcion: "))

    if opcion == 1:
        funciones.agregar_producto(productos)
    elif opcion == 2:
        print()
    elif opcion == 3:
        print()
    elif opcion == 4:
        if len(productos) == 0:
            print("\nNo hay productos cargados en el sistema")
        else:
            for producto in productos:
                print(f"\nProducto: {producto['nombre']}\t Precio: {producto['precio']}\t Stock: {producto['cantidad']}")
    elif opcion == 5:
        print("\nEl programa ha finalizado correctamente\n")
        break
    else:
        print("\nIngrese una opcion valida")