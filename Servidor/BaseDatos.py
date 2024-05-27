import Contacto
import Telefono
import Direccion
import sqlite3

class BaseDatos:
    def __init__(self):
        self.__ruta = 'Contactos.db'
    def LeerContactos(self):
        try:
            database = sqlite3.connect('Contactos.db') #(self.__ruta)
            cursor = database.cursor()

            cursor.execute("SELECT * FROM Contacto")

            contactos = []
            
            for registro in cursor:
                contacto = Contacto.Contacto(registro[0],registro[1],registro[2],registro[3])
                contacto.SetListaTelefonos(self.__LeerTelefonos(database,contacto.GetId()))
                contacto.SetListaDirecciones(self.__LeerDirecciones(database,contacto.GetId()))
                contactos.append(contacto)
                
            database.close()
            return contactos
        except Exception as e:
            print("ERROR: No se pueden leer los contactos - ", e)
            return []
    
    def __LeerTelefonos(self, database, idcontacto):
        try:            
            cursortelefono = database.cursor()
            cursortelefono.execute("SELECT Id,NumeroTelefono,Descripcion FROM Telefono WHERE ContactoId = " + str(idcontacto))

            telefonos = []

            for registro in cursortelefono:
                telefonos.append(Telefono.Telefono(registro[0],registro[1],registro[2]))                
            return telefonos
        except Exception as e:
            print("ERROR: No se pueden leer los teléfonos")
            return []

    def __LeerDirecciones(self, database, idcontacto):
        try:
            cursordireccion = database.cursor()
            cursordireccion.execute("SELECT Id,Calle,Piso,Ciudad,CodigoPostal FROM Direccion WHERE ContactoId = " + str(idcontacto))

            direcciones = []

            for registro in cursordireccion:
                direcciones.append(Direccion.Direccion(registro[0],registro[1],registro[2],registro[3],registro[4]))                
            return direcciones
        except Exception as e:
            print("ERROR: No se pueden leer las direcciones - ", e)
            return []
            
    def LeerContactosNombre(self, nombre):
        try:
            database = sqlite3.connect('Contactos.db')
            cursor = database.cursor()

            cursor.execute("SELECT * FROM Contacto WHERE nombre = '" + nombre + "'")

            contactos = []
            
            for registro in cursor:
                contacto = Contacto.Contacto(registro[0],registro[1],registro[2],registro[3])
                contacto.SetListaTelefonos(self.__LeerTelefonos(database,contacto.GetId()))
                contacto.SetListaDirecciones(self.__LeerDirecciones(database,contacto.GetId()))
                contactos.append(contacto)

            database.close()
            return contactos
        except Exception as e:
            print("ERROR: No se pueden leer contactos por nombre - ", e)
            return []
    
    def LeerContactosTelefono(self, telefono):
        try:
            database = sqlite3.connect('Contactos.db')
            cursor = database.cursor()

            cursor.execute("SELECT DISTINCT * FROM Telefono WHERE NumeroTelefono = '" + telefono + "'")

            contactos = []
            
            for registro in cursor:
                cursorcontacto = database.cursor()
                cursorcontacto.execute("SELECT * FROM Contacto WHERE Id = " + str(registro[1]))

                for registrocontacto in cursorcontacto:            
                    contacto = Contacto.Contacto(registrocontacto[0],registrocontacto[1],registrocontacto[2],registrocontacto[3])
                    contacto.SetListaTelefonos(self.__LeerTelefonos(database,contacto.GetId()))
                    contacto.SetListaDirecciones(self.__LeerDirecciones(database,contacto.GetId()))
                    contactos.append(contacto)

            database.close()
            return contactos
        except Exception as e:
            print("ERROR: No se pueden leer contactos por teléfono - ", e)
            return []
    
    def InsertarContacto(self, contacto):
        try:
            database = sqlite3.connect('Contactos.db')
            cursor = database.cursor()

            infocontacto = (contacto.GetNombre(),contacto.GetApellidos(),contacto.GetFechaNacimiento())
            cursor.execute("INSERT INTO Contacto (Nombre,Apellidos,FechaNacimiento) VALUES(?,?,?)", infocontacto)

            contactoid = cursor.lastrowid
            
            for telefono in contacto.GetListaTelefonos():
                infotelefono = (contactoid,telefono.GetNumeroTelefono(),telefono.GetDescripcion())
                cursor.execute("INSERT INTO Telefono (ContactoId,NumeroTelefono,Descripcion) VALUES(?,?,?)", infotelefono)

            for direccion in contacto.GetListaDirecciones():
                infodireccion = (contactoid,direccion.GetCalle(),direccion.GetPiso(),direccion.GetCiudad(),direccion.GetCodigoPostal())
                cursor.execute("INSERT INTO Direccion (ContactoId,Calle,Piso,Ciudad,CodigoPostal) VALUES(?,?,?,?,?)", infodireccion)
                
            database.commit()
            return True
        except Exception as e:
            print("ERROR: No se puede insertar el contacto - ", e)
            return False
               
    def BorrarContactoId(self, idcontacto):
        try:            
            database = sqlite3.connect('Contactos.db')
            cursor = database.cursor()

            cursor.execute("DELETE FROM Telefono WHERE ContactoId = " + str(idcontacto))
            cursor.execute("DELETE FROM Direccion WHERE ContactoId = " + str(idcontacto))
            cursor.execute("DELETE FROM Contacto WHERE Id = " + str(idcontacto))

            database.commit()
            return True
        except Exception as e:
            print("ERROR: No se puede borrar el contacto - ", e)
            return False
