from src import opciones_menu, menu

while True:
    menu.menu()

    opcion = int(input("\nSelecione una opcion: "))

    if opcion == 1:
        opciones_menu.registrar_producto()
    elif opcion == 2:
        opciones_menu.actualizar_producto()
    elif opcion == 3:
        opciones_menu.eliminar_producto()
    elif opcion == 4:
        opciones_menu.mostrar_productos()
    elif opcion == 5:
        opciones_menu.reporte_bajo_stock()
    elif opcion == 6:
        print("\nEl programa ha finalizado correctamente.\n")
        break
    else:
        print("\nIngrese una opcion valida.")