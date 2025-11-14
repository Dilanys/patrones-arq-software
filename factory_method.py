# =============================================================
#                  PATRÓN 2: FACTORY METHOD
# =============================================================
"""
Este módulo contiene la lógica para crear productos electrónicos básicos 
(Computadora, Teléfono, Tableta) usando fábricas concretas.

"""

class Producto:
    """Clase que modela un producto electrónico básico."""

    def __init__(self, nombre, tipo, precio):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
        self.especificaciones = {}

    def agregar_especificacion(self, clave, valor):
        """Agrega una especificación técnica al producto."""
        self.especificaciones[clave] = valor

    def __str__(self):
        """Representa el producto con sus características."""
        specs = ", ".join(f"{k}: {v}" for k, v in self.especificaciones.items())
        return f"{self.tipo} {self.nombre} (${self.precio}) -> {specs}"


class CreadorProducto:
    """
    Clase base abstracta para definir la interfaz de las fábricas.
    Cada subclase debe implementar crear_producto().
    """
    def crear_producto(self):
        raise NotImplementedError()


class CreadorComputadora(CreadorProducto):
    """Fábrica para productos tipo Computadora."""
    def crear_producto(self):
        p = Producto("Computadora", "Básico", 2000)
        p.agregar_especificacion("RAM", "8GB")
        p.agregar_especificacion("CPU", "Intel i3")
        return p


class CreadorTelefono(CreadorProducto):
    """Fábrica para productos tipo Teléfono."""
    def crear_producto(self):
        p = Producto("Teléfono", "Básico", 900)
        p.agregar_especificacion("Pantalla", "6 pulgadas")
        p.agregar_especificacion("Batería", "4000 mAh")
        return p


class CreadorTableta(CreadorProducto):
    """Fábrica para productos tipo Tableta."""
    def crear_producto(self):
        p = Producto("Tableta", "Básico", 1100)
        p.agregar_especificacion("Pantalla", "10 pulgadas")
        p.agregar_especificacion("RAM", "4GB")
        return p
