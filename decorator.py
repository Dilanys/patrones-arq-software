# =============================================================
#              PATRÓN 5: DECORATOR (Estructural)
# =============================================================
"""
Este patrón permite añadir funcionalidades adicionales a un producto
sin alterar su clase original. Ideal para agregar características como:
- Garantía extendida
- Seguro contra daños
- Envío premium
"""

class ProductoDecorator:
    """
    Decorador base.
    Envuelve un producto existente y delega sus métodos sin modificarlo.
    """
    def __init__(self, producto):
        self._producto = producto

    def __str__(self):
        """Retorna la representación del producto decorado."""
        return str(self._producto)


class GarantiaExtendidaDecorator(ProductoDecorator):
    """Decorador que añade garantía extendida al producto."""
    def __str__(self):
        return f"{super().__str__()} + Garantía Extendida (12 meses)"


class SeguroDañosDecorator(ProductoDecorator):
    """Decorador que añade seguro contra daños accidentales."""
    def __str__(self):
        return f"{super().__str__()} + Seguro contra daños accidental"


class EnvioPremiumDecorator(ProductoDecorator):
    """Decorador que añade envío premium 24 horas."""
    def __str__(self):
        return f"{super().__str__()} + Envío Premium 24h"
