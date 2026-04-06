def mostrar_menu():
    print("\n" + "="*40)
    print("SISTEMA DE INVENTARIO")
    print("="*40)
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")


def mostrar_inventario(inventario):
    if not inventario:
        print("Inventario vacío.")
        return

    for p in inventario:
        print(f"{p['nombre']} - ${p['precio']} - {p['cantidad']}")
