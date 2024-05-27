import Contacto
import Telefono
import Direccion

def StringAContacto(cadena):
    try:
        print(cadena)
        # Obtención de los datos del contacto y creación del objeto con los valores
        datoscontacto = cadena.split("#")[0].split("|")
        contacto = Contacto.Contacto(0,datoscontacto[0],datoscontacto[1],datoscontacto[2])

        # Obtención de los teléfonos y borrado del primer elemento
        # ya que sería vacío al empezar la cadena por #
        datostelefono = cadena.split("#")[1].split("-")
        del datostelefono[0:1]      

        if len(datostelefono)>0:
            telefonos = []
            # Procesamiento de todos los teléfonos y almacenamiento en una lista
            for item in datostelefono:
                telefono = Telefono.Telefono(0,item.split("|")[0],item.split("|")[1])
                telefonos.append(telefono)
            # Añade los teléfonos al contacto
            contacto.SetListaTelefonos(telefonos)
        
        # Obtención de las direcciónes y borrado del primer elemento
        # ya que sería vacío al empezar la cadena por #
        datosdirecciones = cadena.split("#")[2].split("-")
        del datosdirecciones[0:1]      

        if len(datosdirecciones)>0:
            direcciones = []
            # Procesamiento de todas las direcciones y almacenamiento en una lista
            for item in datosdirecciones:
               direccion = Direccion.Direccion(0,item.split("|")[0],item.split("|")[1],item.split("|")[2],item.split("|")[3])
               direcciones.append(direccion)
            # Añade las direcciones a la lista
            contacto.SetListaDirecciones(direcciones)            
        return contacto
    except Exception as e:
        print(f"ERROR: Convirtiendo cadena a contacto - {e}")
        return None

def ContactosAString(contactos):
    try:
        cadena = ""
        # Cada contacto será insertado en la cadena uno a uno
        for contacto in contactos:
            # Datos del contacto
            cadena += "*"
            cadena += contacto.GetNombre()
            cadena += "|"
            cadena += contacto.GetApellidos()
            cadena += "|"
            cadena += contacto.GetFechaNacimiento()
            # Datos de sus teléfonos
            cadena += "#"
            listatelefonos = contacto.GetListaTelefonos()
            if type(listatelefonos) != type(None):
                for telefono in listatelefonos:
                    cadena += "-"
                    cadena += str(telefono.GetNumeroTelefono())
                    cadena += "|"
                    cadena += str(telefono.GetDescripcion())
            # Datos de sus direcciones
            cadena += "#"
            listadirecciones = contacto.GetListaDirecciones()
            if type(listadirecciones) != type(None):
                for direccion in listadirecciones:
                    cadena += "-"
                    cadena += str(direccion.GetCalle())
                    cadena += "|"
                    cadena += str(direccion.GetPiso())
                    cadena += "|"
                    cadena += str(direccion.GetCiudad())
                    cadena += "|"
                    cadena += str(direccion.GetCodigoPostal())
        return cadena
    except Exception as e:
        print(f"ERROR: Convirtiendo el contacto a cadena - {e}")
        return None
