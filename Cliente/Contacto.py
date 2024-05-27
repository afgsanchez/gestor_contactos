import Telefono
import Direccion

class Contacto:
    def __init__(self):
        self.__Id = ""
        self.__Nombre = ""
        self.__Apellidos = ""
        self.__FechaNacimiento = ""
        self.__ListaTelefonos = []
        self.__ListaDirecciones = []
    def GetId(self):
        return self.__Id
    def GetNombre(self):
        return self.__Nombre
    def GetApellidos(self):
        return self.__Apellidos
    def GetFechaNacimiento(self):
        return self.__FechaNacimiento
    def GetListaTelefonos(self):
        return self.__ListaTelefonos
    def GetListaDirecciones(self):
        return self.__ListaDirecciones
    def SetNombre(self, nombre):
        self.__Nombre = nombre
    def SetApellidos(self, apellidos):
        self.__Apellidos = apellidos
    def SetFechaNacimiento(self, fechanacimiento):
        self.__FechaNacimiento = fechanacimiento
    def SetListaTelefonos(self, listatelefonos):
        self.__ListaTelefonos = listatelefonos
    def SetListaDirecciones(self, listadirecciones):
        self.__ListaDirecciones = listadirecciones
