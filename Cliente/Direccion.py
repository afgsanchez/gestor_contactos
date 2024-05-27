class Direccion:
    def __init__(self):
        self.__Id = ""
        self.__Calle = ""
        self.__Piso = ""
        self.__Ciudad = ""
        self.__CodigoPostal = ""
    def GetId(self):
        return self.__Id        
    def GetCalle(self):
        return self.__Calle
    def GetPiso(self):
        return self.__Piso
    def GetCiudad(self):
        return self.__Ciudad
    def GetCodigoPostal(self):
        return self.__CodigoPostal
    def SetCalle(self, calle):
        self.__Calle = calle
    def SetPiso(self, piso):
        self.__Piso = piso
    def SetCiudad(self, ciudad):
        self.__Ciudad = ciudad
    def SetCodigoPostal(self, codigopostal):
        self.__CodigoPostal = codigopostal
