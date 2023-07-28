from Modelos.Persona import Persona
from Repositorio.RepositorioPersona import RepositorioPersona

"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular 
a los modelos, en estos se programarán las tareas básicas tales como crear, listar, 
visualizar, modificar y eliminar. (CRUD)
"""
class ControladorPersona():
    """
    constructor que permite llevar a cabo la creacion de instancias del controlador.
    """
    def __init__(self):
        self.repositorioPersona = RepositorioPersona()
        print("Creando ControladorPersona")

    def index(self):
        print("Listar todos las personas")
        return self.repositorioPersona.findAll()

    def create(self, infoPersona):
        print("Crear una persona")
        nuevaPersona = Persona(infoPersona)
        return self.repositorioPersona.save(nuevaPersona)

    def show(self, id):
        laPersona = Persona(self.repositorioPersona.findById(id))
        return laPersona.__dict__

    def update(self, id, infoPersona):
        personaActual = Persona(self.repositorioPersona.findById(id))
        personaActual.cedulaPersona = infoPersona["cedulaPersona"]
        personaActual.nombrePersona = infoPersona["nombrePersona"]
        personaActual.apellidoPersona = infoPersona["apellidoPersona"]
        return self.repositorioPersona.save(personaActual)

    def delete(self, id):
        print("Elimiando persona con id ", id)
        return self.repositorioPersona.delete(id)
