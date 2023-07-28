from Modelos.Inventario import Inventario
from Modelos.Persona import Persona
from Modelos.Producto import Producto
from Repositorio.RepositorioInventario import RepositorioInventario
from Repositorio.RepositorioPersona import RepositorioPersona
from Repositorio.RepositorioProducto import RepositorioProducto


class ControladorInventario():
    def __init__(self):
        self.repositorioIventario = RepositorioInventario()
        self.repositorioPersona = RepositorioPersona()
        self.repositorioProducto = RepositorioProducto()
        print("Creando ControladorInventario")


    def index(self):
        return self.repositorioIventario.findAll()

    """
    Asignacion persona y producto a inventario
    """

    def create(self, infoInventario, id_persona, id_producto):
        nuevoInventario = Inventario(infoInventario)

        """Instancias para cantidad del producto (tabla producto e inventario)"""
        cantidadProducto = self.repositorioProducto.getObtenerCantidadProducto(id_producto)
        nuevoInventario.cantidadInventario = infoInventario["cantidadInventario"]

        """Instacias para valor del costo de la tabla productos"""
        valorCosto = self.repositorioProducto.getObtenerValorCosto(id_producto)

        """Instacias para valor del venta de la tabla productos"""
        valorVenta = self.repositorioProducto.getObtenervalorVenta(id_producto)


        """Operaciones"""
        """Valor de diferencia inventario"""
        nuevoInventario.diferenciaInventario = (cantidadProducto - nuevoInventario.cantidadInventario)
        """Valor para el total del costo"""
        nuevoInventario.totalCosto = (nuevoInventario.diferenciaInventario * valorCosto)
        """valor para el total de la venta aprox"""
        nuevoInventario.totalVenta = (nuevoInventario.diferenciaInventario * valorVenta)
        """Valor para el margen de ganancias"""
        nuevoInventario.manrgenGanancia = (nuevoInventario.totalVenta - nuevoInventario.totalCosto)

        lafecha = self.repositorioIventario.fecha()
        laPersona = Persona(self.repositorioPersona.findById(id_persona))
        elProducto = Producto(self.repositorioProducto.findById(id_producto))

        nuevoInventario.persona = laPersona
        nuevoInventario.producto = elProducto
        nuevoInventario.fecha = lafecha
        return self.repositorioIventario.save(nuevoInventario)

    def show(self, id):
        elInventario = Inventario(self.repositorioIventario.findById(id))
        return elInventario.__dict__

    """#####obtener un atributo######
    def getUnProducto(self, id_producto, cantidadProducto):
        productos = Inventario(self.repositorioIventario.getCantidadProducto(id_producto, cantidadProducto))
        return productos
    """


    """
    Modificación de inventario (persona y producto)
    """

    def update(self, id, infoInventario, id_persona, id_producto):
        elInventario = Inventario(self.repositorioIventario.findById(id))

        """Instancias para cantidad del producto (tabla producto e inventario)"""
        cantidadProducto = self.repositorioProducto.getObtenerCantidadProducto(id_producto)
        elInventario.cantidadInventario = infoInventario["cantidadInventario"]

        """Instacias para valor del costo de la tabla productos"""
        valorCosto = self.repositorioProducto.getObtenerValorCosto(id_producto)

        """Instacias para valor del venta de la tabla productos"""
        valorVenta = self.repositorioProducto.getObtenervalorVenta(id_producto)

        """Operaciones"""
        """Valor de diferencia inventario"""
        elInventario.diferenciaInventario = (cantidadProducto - elInventario.cantidadInventario)
        """Valor para el total del costo"""
        elInventario.totalCosto = (elInventario.diferenciaInventario * valorCosto)
        """valor para el total de la venta aprox"""
        elInventario.totalVenta = (elInventario.diferenciaInventario * valorVenta)
        """Valor para el margen de ganancias"""
        elInventario.manrgenGanancia = (elInventario.totalVenta - elInventario.totalCosto)

        laPersona = Persona(self.repositorioPersona.findById(id_persona))
        elProducto = Producto(self.repositorioProducto.findById(id_producto))
        elInventario.persona = laPersona
        elInventario.producto = elProducto
        return self.repositorioIventario.save(elInventario)

    def delete(self, id):
        return self.repositorioIventario.delete(id)


