from inventario import *
from csv_utils import *
from ui import *
from utils import *

def main():
    inventario = []

    while True:
        mostrar_menu()
        opcion = input("Opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            precio = input_float("Precio: ")
            cantidad = input_int("Cantidad: ")

            if precio is None or cantidad is None:
                print("Datos inválidos")
                continue

            if agregar_producto(inventario, nombre, precio, cantidad):
                print("Producto agregado")
            else:
                print("Ya existe")

        elif opcion == "2":
            mostrar_inventario(inventario)

        elif opcion == "9":
            break

if __name__ == "__main__":
    main()
