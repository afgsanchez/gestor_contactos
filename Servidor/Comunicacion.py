import socket
import BaseDatos
import Contacto
import Telefono
import Direccion
import Conversion


def HiloCliente(conexion, direccion):
    fin = False
    while not fin:
        try:
            recibido = conexion.recv(1024)
            recibido = recibido.decode('utf-8')

            print("Comando recibido: ", recibido)

            if recibido == "5":
                fin = True

            mensaje = str(ProcesarMensaje(recibido))
            conexion.send(str.encode(mensaje))

        except Exception as e:
            print(f"ERROR: Hilo cliente - {e}")
            fin = True
    conexion.close()

def ProcesarMensaje(mensaje):
    try:
        listamensaje = mensaje.split('&')

        # Buscar contacto por nombre
        if listamensaje[0] == "1" and listamensaje[1] == "1":
            return BuscarContactoNombre(listamensaje[2])
        
        # Buscar contacto por telefono
        if listamensaje[0] == "1" and listamensaje[1] == "2":
            return BuscarContactoTelefono(listamensaje[2])
        
        if listamensaje[0] == "2":
            return CrearContacto(listamensaje[1])
        
        if listamensaje[0] == "3" and listamensaje[1] == "1":
            return BorrarContactoNombre(listamensaje[2])
        
        if listamensaje[0] == "3" and listamensaje[1] == "2":
            return BorrarContactoTelefono(listamensaje[2])
        
        if listamensaje[0] == "4":
            return BuscarTodosLosContactos()
        
    except Exception as e:
        print(f"ERROR: Procesando el mensaje recibido - {e}")
        return ""

def CrearContacto(contactostring):
    try:
        contacto = Conversion.StringAContacto(contactostring.lstrip("*"))
        basedatos = BaseDatos.BaseDatos()
        if basedatos.InsertarContacto(contacto) == True:
            return "1"
        else:
            return "0"
    except Exception as e:
        print(f"ERROR: Creando contacto - {e}")
        return "0"

def BuscarTodosLosContactos():
    try:
            
        basedatos = BaseDatos.BaseDatos()
        datos = basedatos.LeerContactos()
        if len(datos)>0:
            return Conversion.ContactosAString(datos)
        else:
            return "0"
    except Exception as e:
        print(f"ERROR: Buscando todos los contactos - {e}")
        return "0"

def BuscarContactoNombre(nombre):
    try:

        basedatos = BaseDatos.BaseDatos()
        datos = basedatos.LeerContactosNombre(nombre)
        if len(datos)>0:
            return Conversion.ContactosAString(datos)
        else:
            return "0"
    except Exception as e:
        print(f"ERROR: Buscando contacto por nombre - {e}")
        return "0"
 

def BuscarContactoTelefono(telefono):
    try:

        basedatos = BaseDatos.BaseDatos()
        datos = basedatos.LeerContactosTelefono(telefono)
        if len(datos)>0:
            return Conversion.ContactosAString(datos)
        else:
            return "0"
    except Exception as e:
        print(f"ERROR: Buscando contacto por telefono - {e}")
        return "0"       

def BorrarContactoNombre(nombre):
    try:

        basedatos = BaseDatos.BaseDatos()
        datos = basedatos.LeerContactosNombre(nombre)
        respuesta = "1"
        for contacto in datos:
            if basedatos.BorrarContactoId(contacto.GetId()) == False:
                respuesta = "0"
        return respuesta
    except Exception as e:
        print(f"ERROR: Borrando contacto por nombre - {e}")
        return "0"   


def BorrarContactoTelefono(telefono):
    try:

        basedatos = BaseDatos.BaseDatos()
        datos = basedatos.LeerContactosTelefono(telefono)
        respuesta = "1"
        for contacto in datos:
            if basedatos.BorrarContactoId(contacto.GetId()) == False:
                respuesta = "0"
        return respuesta
    except Exception as e:
        print(f"ERROR: Borrando contacto por telefono - {e}")
        return "0"