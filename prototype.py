# =============================================================
#                     PATRÓN 4: PROTOTYPE
# =============================================================
"""
Permite clonar productos existentes y modificar sus especificaciones
sin necesidad de reinstanciar desde cero.
"""

class ProductoPrototype:
    """Define un prototipo que puede clonarse y modificarse."""

    def __init__(self, categoria, linea, precio, especificaciones):
        self.categoria = categoria
        self.linea = linea
        self.precio = precio
        self.especificaciones = dict(especificaciones)

    def clone(self):
        """Crea una copia profunda del prototipo."""
        return ProductoPrototype(self.categoria, self.linea, self.precio, dict(self.especificaciones))

    def modify(self, **cambios):
        """
        Devuelve un clon modificado según los parámetros recibidos.
        Cambios aceptados:
        - precio (int)
        - agregar (dict de especificaciones)
        """
        nuevo = self.clone()
        if "precio" in cambios:
            nuevo.precio = cambios["precio"]
        if "agregar" in cambios:
            for k, v in cambios["agregar"].items():
                nuevo.especificaciones[k] = v
        return nuevo

    def __str__(self):
        """Describe el producto prototipo."""
        spec = ", ".join(f"{k}: {v}" for k, v in self.especificaciones.items())
        return f"[{self.linea}] {self.categoria} (${self.precio}) -> {spec}"


class PrototypeRegistry:
    """Registra prototipos disponibles para clonación rápida."""

    def __init__(self):
        self._reg = {}

    def register(self, key, prototype):
        """Registra un prototipo bajo una clave."""
        self._reg[key] = prototype

    def create(self, key, **mods):
        """Clona y devuelve un prototipo con modificaciones opcionales."""
        return self._reg[key].modify(**mods)
