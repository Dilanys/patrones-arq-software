# =============================================================
#                PATRÓN 3: ABSTRACT FACTORY
# =============================================================
"""
Este patrón permite producir familias completas de productos electrónicos
según una categoría: Premium, Estándar, Económica.

"""

class ProductoLinea:
    """Producto perteneciente a una línea (Premium, Estándar o Económica)."""

    def __init__(self, categoria, linea, precio):
        self.categoria = categoria
        self.linea = linea
        self.precio = precio
        self.especificaciones = {}

    def agregar_especificacion(self, k, v):
        """Añade una especificación técnica al producto."""
        self.especificaciones[k] = v

    def __str__(self):
        """Muestra la información del producto."""
        specs = ", ".join([f"{k}: {v}" for k, v in self.especificaciones.items()])
        return f"[{self.linea}] {self.categoria} (${self.precio}) -> {specs}"


class AbstractLineaFactory:
    """Interfaz que define la creación de productos por línea."""
    def crear_computadora(self): pass
    def crear_telefono(self): pass
    def crear_tableta(self): pass


class LineaPremiumFactory(AbstractLineaFactory):
    """Familia Premium: productos de alto rendimiento."""
    def crear_computadora(self):
        p = ProductoLinea("Computadora", "Premium", 5800)
        p.agregar_especificacion("CPU", "Intel i9")
        p.agregar_especificacion("RAM", "32GB")
        return p

    def crear_telefono(self):
        p = ProductoLinea("Teléfono", "Premium", 3500)
        p.agregar_especificacion("Pantalla", "AMOLED 144Hz")
        return p

    def crear_tableta(self):
        p = ProductoLinea("Tableta", "Premium", 2900)
        p.agregar_especificacion("Pantalla", "12'' HDR")
        return p


class LineaEstandarFactory(AbstractLineaFactory):
    """Familia Estándar: productos con buena relación costo-beneficio."""
    def crear_computadora(self):
        p = ProductoLinea("Computadora", "Estándar", 3000)
        p.agregar_especificacion("CPU", "Intel i5")
        return p

    def crear_telefono(self):
        p = ProductoLinea("Teléfono", "Estándar", 1800)
        p.agregar_especificacion("Pantalla", "OLED")
        return p

    def crear_tableta(self):
        p = ProductoLinea("Tableta", "Estándar", 1500)
        p.agregar_especificacion("RAM", "8GB")
        return p


class LineaEconomicaFactory(AbstractLineaFactory):
    """Familia Económica: productos accesibles y funcionales."""
    def crear_computadora(self):
        p = ProductoLinea("Computadora", "Económica", 1300)
        p.agregar_especificacion("CPU", "Intel Celeron")
        return p

    def crear_telefono(self):
        p = ProductoLinea("Teléfono", "Económica", 700)
        p.agregar_especificacion("Pantalla", "LCD")
        return p

    def crear_tableta(self):
        p = ProductoLinea("Tableta", "Económica", 600)
        p.agregar_especificacion("RAM", "4GB")
        return p
