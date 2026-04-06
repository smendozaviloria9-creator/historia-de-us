def agregar_producto(inventario, nombre, precio, cantidad):
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return False
    inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    return True


def buscar_producto(inventario, nombre):
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return producto
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    producto = buscar_producto(inventario, nombre)
    if producto:
        if nuevo_precio is not None:
            producto["precio"] = nuevo_precio
        if nueva_cantidad is not None:
            producto["cantidad"] = nueva_cantidad
        return True
    return False


def eliminar_producto(inventario, nombre):
    producto = buscar_producto(inventario, nombre)
    if producto:
        inventario.remove(producto)
        return True
    return False


def calcular_estadisticas(inventario):
    if not inventario:
        return {
            "unidades_totales": 0,
            "valor_total": 0.0,
            "producto_mas_caro": None,
            "producto_mayor_stock": None
        }

    subtotal = lambda p: p["precio"] * p["cantidad"]

    return {
        "unidades_totales": sum(p["cantidad"] for p in inventario),
        "valor_total": sum(subtotal(p) for p in inventario),
        "producto_mas_caro": max(inventario, key=lambda p: p["precio"]),
        "producto_mayor_stock": max(inventario, key=lambda p: p["cantidad"])
    }
