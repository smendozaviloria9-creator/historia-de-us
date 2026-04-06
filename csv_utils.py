import csv
import os

def guardar_csv(inventario, ruta, incluir_header=True):
    """Guarda el inventario en un archivo CSV."""
    if not inventario:
        print("Error: No se puede guardar un inventario vacío.")
        return False
    try:
        directorio = os.path.dirname(ruta) if os.path.dirname(ruta) else "."
        if not os.access(directorio, os.W_OK):
            print(f"Error: No se tienen permisos de escritura en {directorio}")
            return False
        with open(ruta, 'w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo, delimiter=',')
            if incluir_header:
                escritor.writerow(["nombre", "precio", "cantidad"])
            for producto in inventario:
                escritor.writerow([producto["nombre"], producto["precio"], producto["cantidad"]])
        print(f"Inventario guardado en: {ruta}")
        return True
    except PermissionError:
        print(f"Error: Permiso denegado al escribir en {ruta}")
        return False
    except Exception as e:
        print(f"Error inesperado al guardar el archivo: {e}")
        return False

def cargar_csv(ruta):
    """Carga un inventario desde un archivo CSV."""
    productos_cargados = []
    filas_invalidas = 0
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo, delimiter=',')
            filas = list(lector)
            if len(filas) < 1:
                print("Error: El archivo está vacío.")
                return []
            encabezado = [col.lower().strip() for col in filas[0]]
            if encabezado != ["nombre", "precio", "cantidad"]:
                print(f"Error: Encabezado inválido. Se esperaba 'nombre,precio,cantidad'")
                return []
            for i, fila in enumerate(filas[1:], 1):
                if len(fila) != 3:
                    filas_invalidas += 1
                    continue
                nombre, precio_str, cantidad_str = fila
                nombre = nombre.strip()
                if not nombre:
                    filas_invalidas += 1
                    continue
                try:
                    precio = float(precio_str)
                    cantidad = int(cantidad_str)
                    if precio < 0 or cantidad < 0:
                        filas_invalidas += 1
                        continue
                    productos_cargados.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
                except ValueError:
                    filas_invalidas += 1
                    continue
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta}'")
        return []
    except UnicodeDecodeError:
        print(f"Error: No se pudo leer el archivo '{ruta}'. Codificación incorrecta.")
        return []
    except Exception as e:
        print(f"Error inesperado al leer el archivo: {e}")
        return []
    
    accion = input(f"¿Sobrescribir inventario actual? (S/N): ").strip().upper()
    print(f"\nResumen de carga:")
    print(f"Productos cargados: {len(productos_cargados)}")
    if filas_invalidas > 0:
        print(f"Filas inválidas omitidas: {filas_invalidas}")
    print(f"Acción: {'Sobrescribir' if accion == 'S' else 'Fusionar'}")
    return productos_cargados
        return inventario

    except Exception as e:
        print(f"Error: {e}")
        return []
