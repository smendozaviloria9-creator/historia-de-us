import csv
import os

def guardar_csv(inventario, ruta, incluir_header=True):
    if not inventario:
        print("Inventario vacío.")
        return False

    try:
        with open(ruta, 'w', newline='', encoding='utf-8') as archivo:
            writer = csv.writer(archivo)
            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])

            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def cargar_csv(ruta):
    inventario = []

    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            reader = csv.reader(archivo)
            next(reader)  # saltar encabezado

            for fila in reader:
                nombre, precio, cantidad = fila
                inventario.append({
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                })

        return inventario

    except Exception as e:
        print(f"Error: {e}")
        return []
