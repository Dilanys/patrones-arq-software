# =============================================================
#                     PATRÓN 1: SINGLETON
# =============================================================
"""

Este módulo define la clase AppConfig, responsable de manejar la 
configuración global de la aplicación. El patrón Singleton garantiza 
que únicamente exista un objeto de configuración durante toda la 
ejecución del programa, asegurando consistencia entre todas las partes 
del sistema que dependen del estado global.

"""

class AppConfig:
    """Clase que implementa el patrón Singleton para configuración global."""
    
    _instance = None  # referencia estática a la única instancia

    def __new__(cls, *args, **kwargs):
        """
        Controla la creación del objeto. Si no existe una instancia previa, 
        se crea una. Si ya existe, se reutiliza la existente.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, entorno="producción", idioma="es", debug=False):
        """
        Inicializa los valores de configuración global. Se usa un atributo 
        "_initialized" para evitar reejecuciones de __init__ en posteriores llamadas.
        """
        if not hasattr(self, "_initialized"):
            self.entorno = entorno
            self.idioma = idioma
            self.debug = debug
            self._initialized = True

    def actualizar(self, **kwargs):
        """
        Actualiza dinámicamente cualquier atributo de configuración.
        Parámetros clave-valor.
        """
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        """Retorna una representación legible del estado actual de la configuración."""
        return f"[Configuración] entorno={self.entorno}, idioma={self.idioma}, debug={self.debug}"
