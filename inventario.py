def agregar_producto(inventario, nombre, precio, cantidad):
    """Agrega un nuevo producto al inventario."""
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return False
    inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    return True

def mostrar_inventario(inventario):
    """Muestra todos los productos del inventario."""
    if not inventario:
        print("El inventario está vacío.")
        return
    print("\n" + "="*50)
    print("INVENTARIO ACTUAL")
    print("="*50)
    for producto in inventario:
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: ${producto['precio']:.2f}")
        print(f"Cantidad: {producto['cantidad']}")
        print("-" * 30)

def buscar_producto(inventario, nombre):
    """Busca un producto por nombre."""
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return producto
    return None

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """Actualiza el precio y/o cantidad de un producto."""
    producto = buscar_producto(inventario, nombre)
    if producto:
        if nuevo_precio is not None:
            producto["precio"] = nuevo_precio
        if nueva_cantidad is not None:
            producto["cantidad"] = nueva_cantidad
        return True
    return False

def eliminar_producto(inventario, nombre):
    """Elimina un producto del inventario."""
    producto = buscar_producto(inventario, nombre)
    if producto:
        inventario.remove(producto)
        return True
    return False

def calcular_estadisticas(inventario):
    """Calcula estadísticas del inventario."""
    if not inventario:
        return {"unidades_totales": 0, "valor_total": 0.0, "producto_mas_caro": None, "producto_mayor_stock": None}
    
    subtotal = lambda p: p["precio"] * p["cantidad"]
    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(subtotal(p) for p in inventario)
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])
    
    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock}
