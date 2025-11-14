"""
Archivo principal del sistema de gestión de productos electrónicos.

Este módulo coordina la interacción entre todos los patrones implementados:
- Singleton (AppConfig)
- Factory Method (creación básica)
- Abstract Factory (familias completas)
- Prototype (clonación y variantes)
- Decorator (extensiones opcionales)
- Menús interactivos
"""

from singleton import AppConfig
from factory_method import CreadorComputadora, CreadorTelefono, CreadorTableta
from abstract_factory import (
    LineaPremiumFactory, LineaEstandarFactory, LineaEconomicaFactory
)
from prototype import PrototypeRegistry, ProductoPrototype
from menus import menu_principal, menu_tipo_producto, menu_lineas, menu_clon


def main():
    """Función principal que controla el flujo del programa."""

    # Registro de prototipos
    registry = PrototypeRegistry()
    registry.register("tel_premium",
        ProductoPrototype("Teléfono", "Premium", 3500, {"Pantalla": "AMOLED", "Batería": "5000mAh"})
    )
    registry.register("pc_estandar",
        ProductoPrototype("Computadora", "Estándar", 3000, {"RAM": "16GB", "CPU": "Intel i5"})
    )

    while True:
        opcion = menu_principal()

        # FACTORY METHOD
        if opcion == "1":
            tipo = menu_tipo_producto()
            if tipo == "1":
                print(CreadorComputadora().crear_producto())
            elif tipo == "2":
                print(CreadorTelefono().crear_producto())
            elif tipo == "3":
                print(CreadorTableta().crear_producto())
            else:
                print("Opción inválida.")

        # ABSTRACT FACTORY
        elif opcion == "2":
            linea = menu_lineas()
            if linea == "1":
                factory = LineaPremiumFactory()
            elif linea == "2":
                factory = LineaEstandarFactory()
            else:
                factory = LineaEconomicaFactory()

            tipo = menu_tipo_producto()
            if tipo == "1":
                print(factory.crear_computadora())
            elif tipo == "2":
                print(factory.crear_telefono())
            elif tipo == "3":
                print(factory.crear_tableta())
            else:
                print("Opción inválida.")

        # PROTOTYPE
        elif opcion == "3":
            clon = menu_clon()
            if clon == "1":
                print(registry.create("tel_premium", agregar={"Color": "Rojo"}, precio=2999))
            elif clon == "2":
                print(registry.create("pc_estandar", agregar={"SSD": "1TB"}, precio=3200))
            else:
                print("Opción inválida.")

        # SINGLETON - VER CONFIG
        elif opcion == "4":
            print(AppConfig())

        # SINGLETON - CAMBIAR CONFIG
        elif opcion == "5":
            campo = input("Campo a cambiar (entorno/idioma/debug): ")
            valor = input("Nuevo valor: ")
            if campo == "debug":
                valor = valor.lower() == "true"
            AppConfig().actualizar(**{campo: valor})
            print("Configuración actualizada.")

        elif opcion == "6":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
