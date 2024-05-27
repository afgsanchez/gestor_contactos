class Telefono:
    def __init__(self,idtelefono,numerotelefono,descripcion):
        self.__Id = idtelefono
        self.__NumeroTelefono = numerotelefono
        self.__Descripcion = descripcion
    def GetId(self):
        return self.__Id
    def GetNumeroTelefono(self):
        return self.__NumeroTelefono
    def GetDescripcion(self):
        return self.__Descripcion
    def SetNumeroTelefono(self, telefono):
        self.__NumeroTelefono = telefono
    def SetDescripcion(self, descripcion):
        self.__Descripcion = descripcion
