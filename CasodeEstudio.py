import time
from collections import namedtuple
from functools import wraps


class ProductoNoEncontrado(Exception):
    pass

class StockInsuficiente(Exception):
    pass

# Decoradores
def registrar_operacion(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Ejecutando: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def medir_tiempo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"[TIEMPO] {func.__name__} tomó {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

# Clase Producto
class Producto:
    contador = 1 
    def __init__(self, codigo, nombre, precio, stock, categoria, tipo=None, fecha_vencimiento=None, garantia=None):
        self.codigo = codigo or Producto.contador
        Producto.contador += 1
        self.nombre = nombre
        self.precio = precio
        self._stock = stock
        self.__categoria = categoria
        self.tipo = tipo
        self.fecha_vencimiento = fecha_vencimiento
        self.garantia = garantia

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, valor):
        if valor < 0:
            raise ValueError("El stock no puede ser negativo")
        self._stock = valor

    @property
    def categoria(self):
        return self.__categoria

    def __repr__(self):
        return f"Producto({self.codigo}, {self.nombre}, {self.precio}, Stock: {self.stock}, Categoría: {self.categoria})"


productos = []

@registrar_operacion
def cargar_productos(lista_datos):
    for datos in lista_datos:
        try:
            producto = Producto(*datos)
            productos.append(producto)
        except Exception as e:
            print(f"Error al cargar producto: {e}")

@registrar_operacion
def eliminar_producto(codigo):
    global productos
    productos = [p for p in productos if p.codigo != codigo]
    print(f"Producto con código {codigo} eliminado.")

@registrar_operacion
def aplicar_descuento(porcentaje):
    def descuento(prod):
        prod.precio *= (1 - porcentaje / 100)
        return prod
    return list(map(descuento, productos))

@registrar_operacion
@medir_tiempo
def valor_total_inventario():
    return sum(p.precio * p.stock for p in productos)

@registrar_operacion
def generar_reporte():
    for p in productos:
        codigo, nombre, precio, stock, cat = p.codigo, p.nombre, p.precio, p.stock, p.categoria
        print(f"{codigo} - {nombre} - ${precio:.2f} - Stock: {stock} - {cat}")


if __name__ == "__main__":
    datos = [
        (1, "Laptop", 2500, 5, "Electrónica", "Computadora", None, "1 año"),
        (2, "Silla", 150, 10, "Muebles", "Oficina"),
        (3, "Teléfono", 800, 7, "Electrónica", "Móvil", None, "6 meses"),
    ]

    cargar_productos(datos)
    generar_reporte()
    aplicar_descuento(10)
    print("\nDespués de aplicar descuento:")
    generar_reporte()
    print(f"\nValor total del inventario: ${valor_total_inventario():.2f}")
    
    eliminar_producto(2)
    print("\nDespués de eliminar producto con código 2:")
    generar_reporte()
