historia de usuario 
#sebastian mendoza
Características
CRUD Completo: Agregar, buscar, actualizar y eliminar productos.
Validación de Datos: Control de precios y cantidades negativas, así como entradas no numéricas.
Persistencia de Datos: Importación y exportación de inventario mediante archivos CSV.
Inteligencia de Carga: Opción de sobrescribir el inventario actual o fusionarlo (sumando stock de productos existentes).
Estadísticas: Cálculo automático de valor total del inventario, unidades totales, producto más caro y producto con mayor stock.

 Requisitos
Python 3.x
Módulos estándar: csv, os (no requieren instalación adicional).

 Instalación y Uso
Ejecuta el programa desde tu terminal:



python inventario.py
Al iniciar el programa, verás un menú interactivo:
Agregar producto: Solicita nombre, precio y cantidad. No permite nombres duplicados.
Mostrar inventario: Lista todos los productos con un formato limpio.
Buscar producto: Localización rápida por nombre (no distingue mayúsculas).
Actualizar producto: Permite cambiar el precio o la cantidad de un ítem existente.
Eliminar producto: Quita un producto del registro permanentemente.
Ver estadísticas: Resumen financiero del negocio.
Guardar/Cargar CSV: Ideal para respaldar la información o trabajar con tablas externas.
