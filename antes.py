
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
        self,
        nombre: str,
        precio: str,
        stock: str,
        categoria: str,
        tipo: str,
        codigo: str = "9999",
        fecha_vencimiento: str = None,
        garantia: str = None
    ) -> None:
        self.__codigo: str = codigo
        self._nombre: str = nombre
        self._precio: float = precio
        self.__stock: str = stock
        self.categoria: str = categoria
        self.tipo: str = tipo
        self._fecha_vencimiento: str = fecha_vencimiento
        self.__garantia: str = garantia
    
    @property
    def codigo(self) -> str:
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo: str) -> None:
        if len(codigo) != 100:
            self.__codigo = "9999"
        else:
            self.__codigo = codigo

    @property
    def garantia(self) -> str:
        return self.__garantia
    @garantia.setter
    def garantia(self, garantia, categoria: str) -> None:
        if garantia != categoria:
            return self.__garantia 
        else:
            self.__garantia = "Tiene garantia"

    def mostrardatos(self) -> str:
        return (
            f"codigo: {self.codigo}\n"
            f"nombre: {self._nombre}\n"
            f"precio: {self._precio}\n"
            f"stock: {self.__stock}"
        )

if __name__:
    producto1 = Producto("Helado", 2.50, "Disponible","Variado", "Dulce")
    
    print(producto1.mostrardatos())
    
    