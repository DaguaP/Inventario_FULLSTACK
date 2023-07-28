from Repositorio.RepositorioProducto import RepositorioProducto
from Repositorio.RepositorioProveedor import RepositorioProveedor
from Controladores.ControladorProducto import ControladorProducto
from Modelos.Producto import Producto
from Modelos.Proveedor import Proveedor



class ControladorProveedor():
    def __init__(self):
        self.repositorioProveedor = RepositorioProveedor()
        self.repositorioProducto = RepositorioProducto()
        print("Creando ControladorProveerdor")

    def index(self):
        return self.repositorioProveedor.findAll()

    def create(self, infoProveedor):
        nuevoProveedor = Proveedor(infoProveedor)
        return self.repositorioProveedor.save(nuevoProveedor)

    def show(self, id):
        elProveedor = Proveedor(self.repositorioProveedor.findById(id))
        return elProveedor.__dict__

    def update(self, id, infoProveedor):
        ProveedorActual = Proveedor(self.repositorioProveedor.findById(id))
        ProveedorActual.nombreProveedor = infoProveedor["nombreProveedor"]
        ProveedorActual.telefonoProveedor = infoProveedor["telefonoProveedor"]
        ProveedorActual.nombreEmpresa = infoProveedor["nombreEmpresa"]
        return self.repositorioProveedor.save(ProveedorActual)

    def delete(self, id):
        return self.repositorioProveedor.delete(id)

    #def getProductos(self, id):
    #    productoActual = Producto(self.repositorioProducto.findAll())
    #   proveedorActual = Proveedor(self.repositorioProveedor.findById(id))
    #   proveedorActual.producto = productoActual
    #   proveedorActual.proveedor = productoActual
    #   return self.repositorioProveedor.findAll(proveedorActual)

