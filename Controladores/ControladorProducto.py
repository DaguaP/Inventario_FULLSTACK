from Repositorio.RepositorioProducto import RepositorioProducto
from Repositorio.RepositorioProveedor import RepositorioProveedor
from Modelos.Producto import Producto
from Modelos.Proveedor import Proveedor



class ControladorProducto():
    def __init__(self):
        self.repositorioProducto = RepositorioProducto()
        self.repositorioProveedor = RepositorioProveedor()
        print("Creando ControladorProducto")

    def index(self):
        return self.repositorioProducto.findAll()

    def create(self, infoProducto):
        nuevoProducto = Producto(infoProducto)
        nuevoProducto.valorCosto = infoProducto["valorCosto"]
        nuevoProducto.cantidadProducto = infoProducto["cantidadProducto"]
        nuevoProducto.totalCompra = (nuevoProducto.valorCosto * nuevoProducto.cantidadProducto)
        return self.repositorioProducto.save(nuevoProducto)

    def show(self, id):
        elProducto = Producto(self.repositorioProducto.findById(id))
        return elProducto.__dict__

    def update(self, id, infoProducto):
        productoActual = Producto(self.repositorioProducto.findById(id))
        productoActual.nombreProducto = infoProducto["nombreProducto"]
        productoActual.descripcionProducto = infoProducto["descripcionProducto"]
        productoActual.cantidadProducto = infoProducto["cantidadProducto"]
        productoActual.cantidadUnitaria = infoProducto["cantidadUnitaria"]
        productoActual.valorCosto = infoProducto["valorCosto"]
        productoActual.valorVenta = infoProducto["valorVenta"]
        productoActual.totalCompra = (productoActual.valorCosto * productoActual.cantidadProducto)
        return self.repositorioProducto.save(productoActual)

    def delete(self, id):
        return self.repositorioProducto.delete(id)

    """
    Relación proveedor y producto
    """
    def asignarProveedor(self, id, id_proveedor):
        productoActual = Producto(self.repositorioProducto.findById(id))
        proveedorActual = Proveedor(self.repositorioProveedor.findById(id_proveedor))
        productoActual.proveedor = proveedorActual
        return self.repositorioProducto.save(productoActual)


