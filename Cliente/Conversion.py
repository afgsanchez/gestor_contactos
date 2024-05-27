import Contacto
import Telefono
import Direccion

def ContactoAString(contacto):
    try:
        cadena = ""
        # Inserta en la cadena los datos del contacto
        cadena += "*"
        cadena += contacto.GetNombre()
        cadena += "|"
        cadena += contacto.GetApellidos()
        cadena += "|"
        cadena += contacto.GetFechaNacimiento()
        # Inserta en la cadena los datos de los teléfonos
        cadena += "#"
        listatelefonos = contacto.GetListaTelefonos()
        if type(listatelefonos) != type(None):
            for telefono in listatelefonos:
                cadena += "-"
                cadena += str(telefono.GetNumeroTelefono())
                cadena += "|"
                cadena += str(telefono.GetDescripcion())
        # Inserta en la cadena los datos de las direcciones
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
    except:
        print("ERROR: Convirtiendo el contacto a cadena")
        return None
