from src import opciones_menu
from src import menu

productos = []

while True:
    menu.menu()

    opcion = int(input("Selecione una opcion: "))

    if opcion == 1:
        opciones_menu.registrar_producto(productos)
    elif opcion == 2:
        opciones_menu.actualizar_producto(productos)
    elif opcion == 3:
        opciones_menu.eliminar_producto(productos)
    elif opcion == 4:
        opciones_menu.mostrar_productos(productos)
    elif opcion == 5:
        opciones_menu.reporte_bajo_stock(productos)
    elif opcion == 6:
        print("\nEl programa ha finalizado correctamente\n")
        break
    else:
        print("\nIngrese una opcion valida")