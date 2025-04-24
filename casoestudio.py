# Caso de Estudio: Sistema de Gestión de
# Productos
# Objetivo
# Desarrollar una clase de productos utilizando conceptos de Python como unpacking,
# map, sum, excepciones, decoradores y colecciones, pero sin implementar herencia.
# Requerimientos
# 1. Clase Producto
# • Crear una única clase Producto con atributos como código, nombre, precio,
# stock, categoría y atributos adicionales como tipo, fecha_vencimiento (opcional)
# y garantía (opcional). Crear atributos públicos, protegidos y privados con sus
# respectivos properties. Además métodos de usuario según las especificaciones
# 2. Uso de unpacking
# • Implementar la carga de productos desde tuplas de datos utilizando unpacking.
# • Utilizar unpacking para extraer información de ventas y reportes.
# 3. Utilización de map y sum
# • Usar map para aplicar descuentos a múltiples productos.
# • Implementar sum para calcular el valor total del inventario.
# 4. Excepciones personalizadas
# • Crear excepciones específicas para manejar errores de operaciones con
# productos.
# 5. Decoradores
# • Implementar decoradores para registrar operaciones y medir tiempos de
# ejecución.
# 6. Colecciones
# • Usar diferentes colecciones (listas, diccionarios, tuplas) para gestionar los datos.
# Tareas específicas
# 1. Crear la clase
# 2. Implementar una función para cargar productos mediante unpacking desde una
# lista de datos.
# 3. Crear un método para aplicar descuentos masivos usando map.
# 4. Desarrollar funciones para calcular totales con sum.
# 5. Implementar decoradores para validaciones y registro de operaciones.
# 6. Crear un sistema de manejo de excepciones para las operaciones.
# 7. Desarrollar métodos para generar reportes utilizando unpacking y map.
class Producto:
    def __init__(
        self,nombre: str, 
        precio: str, 
        stock: str, 
        categoria: str,
        codigo: str = "99999999",
        tipo: str = None,
        fecha_vencimiento: str = None,
        garantia: str = None
        
        ) -> None:

        self.codigo = codigo
        self.nombre = nombre
        self.__precio = precio
        self.__stock = stock
        self.categoria = categoria
        self._tipo = tipo
        self.fecha_vencimiento = fecha_vencimiento
        self.__garantia = garantia
    
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio <= 0:
            raise ValueError("El precio no puede ser negativo")
        self.__precio = nuevo_precio

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, nuevo_stock):
        if nuevo_stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        self.__stock = nuevo_stock

    @property
    def garantia(self):
        return self.__garantia
    
    def mostrar_datos(self) -> str:
        return (
            f"Producto: {self.nombre}\n"
            f"Precio: ${self.precio}\n"
            f"Stock: {self.stock} unidades\n"
            f"Categoría: {self.categoria}\n"
            f"Tipo: {self._tipo or 'No especificado'}\n"
            f"Fecha de vencimiento: {self.fecha_vencimiento or 'No aplica'}\n"
            f"Garantía: {self.__garantia or 'No aplica'}\n"
            f"Código: {self.codigo}"
        )

    # def mostrar_datos(self) -> str:
    #     produc_info: str = f"stock: {self.__stock}" if self.__stock else "Producto: No proporcionado"
    #     return (
    #         f"Datos de la Persona:\n"
    #         f"Nombre producto: {self.nombre}\n"
    #         f"Precio: {self.__precio}\n"
    #         f"Codigo: {self.codigo}\n"
    #         f"{produc_info}"
    #     )
    
if __name__ == "__main__":
    producto1 = Producto("Pera", -25, "Disponible", "Fruta", "9999999")
    print(producto1.mostrar_datos())
    