from inventario import *
from csv_utils import *
from ui import *
from utils import *

def main():
    """Función principal del programa."""
    inventario = []
    while True:
        try:
            mostrar_menu()
            opcion = input("Seleccione una opción (1-9): ").strip()
            if opcion == "1":
                nombre = input("Nombre del producto: ").strip()
                if not nombre:
                    print("El nombre no puede estar vacío.")
                    continue
                try:
                    precio = float(input("Precio: "))
                    if precio < 0:
                        print("El precio no puede ser negativo.")
                        continue
                    cantidad = int(input("Cantidad: "))
                    if cantidad < 0:
                        print("La cantidad no puede ser negativa.")
                        continue
                    if agregar_producto(inventario, nombre, precio, cantidad):
                        print(f"Producto '{nombre}' agregado correctamente.")
                    else:
                        print(f"Error: Ya existe un producto con el nombre '{nombre}'.")
                except ValueError:
                    print("Error: Precio y cantidad deben ser numéricos.")
            elif opcion == "2":
                mostrar_inventario(inventario)
            elif opcion == "3":
                nombre = input("Nombre del producto a buscar: ").strip()
                producto = buscar_producto(inventario, nombre)
                if producto:
                    print(f"\nProducto encontrado:")
                    print(f"Nombre: {producto['nombre']}")
                    print(f"Precio: ${producto['precio']:.2f}")
                    print(f"Cantidad: {producto['cantidad']}")
                else:
                    print(f"Producto '{nombre}' no encontrado.")
            elif opcion == "4":
                nombre = input("Nombre del producto a actualizar: ").strip()
                producto = buscar_producto(inventario, nombre)
                if not producto:
                    print(f"Producto '{nombre}' no encontrado.")
                    continue
                print(f"Producto actual: {producto['nombre']} - ${producto['precio']:.2f} - {producto['cantidad']} unidades")
                actualizar_precio = input("¿Actualizar precio? (S/N): ").strip().upper() == "S"
                nuevo_precio = None
                if actualizar_precio:
                    try:
                        nuevo_precio = float(input("Nuevo precio: "))
                        if nuevo_precio < 0:
                            print("El precio no puede ser negativo.")
                            continue
                    except ValueError:
                        print("Precio inválido.")
                        continue
                actualizar_cantidad = input("¿Actualizar cantidad? (S/N): ").strip().upper() == "S"
                nueva_cantidad = None
                if actualizar_cantidad:
                    try:
                        nueva_cantidad = int(input("Nueva cantidad: "))
                        if nueva_cantidad < 0:
                            print("La cantidad no puede ser negativa.")
                            continue
                    except ValueError:
                        print("Cantidad inválida.")
                        continue
                if actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad):
                    print(f"Producto '{nombre}' actualizado correctamente.")
                else:
                    print("Error al actualizar el producto.")
            elif opcion == "5":
                nombre = input("Nombre del producto a eliminar: ").strip()
                if eliminar_producto(inventario, nombre):
                    print(f"Producto '{nombre}' eliminado correctamente.")
                else:
                    print(f"Producto '{nombre}' no encontrado.")
            elif opcion == "6":
                estadisticas = calcular_estadisticas(inventario)
                print(f"\nESTADÍSTICAS DEL INVENTARIO")
                print(f"-"*40)
                print(f"Unidades totales: {estadisticas['unidades_totales']}")
                print(f"Valor total: ${estadisticas['valor_total']:.2f}")
                if estadisticas['producto_mas_caro']:
                    p = estadisticas['producto_mas_caro']
                    print(f"Producto más caro: {p['nombre']} (${p['precio']:.2f})")
                else:
                    print("Producto más caro: -")
                if estadisticas['producto_mayor_stock']:
                    p = estadisticas['producto_mayor_stock']
                    print(f"Mayor stock: {p['nombre']} ({p['cantidad']} unidades)")
                else:
                    print("Mayor stock: -")
            elif opcion == "7":
                ruta = input("Ruta del archivo CSV para guardar: ").strip()
                if ruta:
                    guardar_csv(inventario, ruta)
                else:
                    print("Ruta no válida.")
            elif opcion == "8":
                ruta = input("Ruta del archivo CSV para cargar: ").strip()
                if ruta:
                    nuevos_productos = cargar_csv(ruta)
                    if nuevos_productos:
                        accion = input("¿Sobrescribir inventario actual? (S/N): ").strip().upper()
                        if accion == "S":
                            inventario = nuevos_productos
                            print("Inventario sobrescrito correctamente.")
                        else:
                            fusionados = 0
                            for nuevo_prod in nuevos_productos:
                                encontrado = False
                                for prod in inventario:
                                    if prod["nombre"].lower() == nuevo_prod["nombre"].lower():
                                        prod["cantidad"] += nuevo_prod["cantidad"]
                                        if prod["precio"] != nuevo_prod["precio"]:
                                            prod["precio"] = nuevo_prod["precio"]
                                        encontrado = True
                                        fusionados += 1
                                        break
                                if not encontrado:
                                    inventario.append(nuevo_prod)
                                    fusionados += 1
                            print(f"Inventario fusionado. {fusionados} productos procesados.")
                else:
                    print("Ruta no válida.")
            elif opcion == "9":
                print("Gracias por usar el sistema de inventario. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción entre 1 y 9.")
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario. Saliendo...")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")

if _name_ == "_main_":
    main()   


# 5. Documentación del código:
# Este programa permite gestionar el ingreso de mercancía básica, asegurando que los
# cálculos financieros sean precisos mediante la validación de tipos de datos.
