# =============================================================
#                     MENÚS INTERACTIVOS
# =============================================================
"""
Contiene las funciones encargadas de mostrar los menús interactivos del sistema 
y recopilar la opción seleccionada por el usuario.
"""

def menu_principal():
    """Muestra el menú principal del sistema."""
    print("""
===============================
📦 Sistema de Gestión de Productos
       (Patrones Creacionales)
===============================

1. Crear producto básico (Factory Method)
2. Crear producto por línea (Abstract Factory)
3. Clonar producto (Prototype)
4. Ver configuración del sistema (Singleton)
5. Cambiar configuración del sistema (Singleton)
6. Salir
""")
    return input("Seleccione una opción: ")


def menu_tipo_producto():
    """Pregunta qué tipo de producto desea crear."""
    print("""
¿Qué tipo de producto desea?

1. Computadora
2. Teléfono
3. Tableta
""")
    return input("Seleccione una opción: ")


def menu_lineas():
    """Selecciona la línea completa de productos."""
    print("""
Seleccione la línea de productos:

1. Premium
2. Estándar
3. Económica
""")
    return input("Seleccione una opción: ")


def menu_clon():
    """Muestra los prototipos disponibles para clonar."""
    print("""
Seleccione un prototipo a clonar:

1. Teléfono Premium
2. Computadora Estándar
""")
    return input("Seleccione una opción: ")
