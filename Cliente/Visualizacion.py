import Contacto
import Telefono
import Direccion
import Conversion

def MostrarMenu():
    print ("""Menu
1) Ver contacto
2) Crear contacto nuevo
3) Borrar contacto
4) Mostrar todos los contactos
5) Salir""")

def MostrarMenuBuscar():
    print ("""Buscar contactos:
1) Nombre
2) Telefono
3) Volver""")

def MostrarMenuBorrar():
    print ("""Borrar contactos por:
1) Nombre
2) Telefono
3) Volver""")

def ObtenerOpcion(texto):
    leido = False
    while not leido:
        try:
            numero = int(input(texto))
        except ValueError:
            print("Error: Tienes que introducir un numero.")
        else:
            leido = True
    return numero

def MostrarContactos(contactos):
    try:
        print("##### CONTACTOS #####")

        # Obtención de los diferentes contactos y borrado del primer elemento
        # ya que sería vacío al empezar la cadena por *
        cadena = contactos.split("*")
        del cadena[0:1]    

        for contacto in cadena:
            print("-- Contacto --")
            # Datos del contacto
            datoscontacto = contacto.split("#")[0].split("|")
            print("Nombre: ",datoscontacto[0])
            print("Apellidos: ",datoscontacto[1])
            print("Fecha de Nacimiento: ",datoscontacto[2])

            # Obtención de los teléfonos y borrado del primer elemento
            # ya que sería vacío al empezar la cadena por #
            datostelefono = contacto.split("#")[1].split("-")
            del datostelefono[0:1]      
            
            if len(datostelefono)>0:
                for telefono in datostelefono:
                    print("Telefono: ", telefono.split("|")[0], "(",telefono.split("|")[1],")")        

            # Obtención de las direcciónes y borrado del primer elemento
            # ya que sería vacío al empezar la cadena por #
            datosdirecciones = contacto.split("#")[2].split("-")
            del datosdirecciones[0:1]      

            if len(datosdirecciones)>0:
                for direccion in datosdirecciones:
                    print("Dirección: ", direccion.split("|")[0],direccion.split("|")[1],",",direccion.split("|")[2],",",direccion.split("|")[3])
            
        print("#####################")
    except:
        print("ERROR: No se pueden mostrar los contactos")        

def ProcesoCrearContacto():
    try:        
        print("##### NUEVO CONTACTO #####")
        
        nuevocontacto = Contacto.Contacto()
        nuevocontacto.SetNombre(input((">Introduce el nombre del contacto: ")))
        nuevocontacto.SetApellidos(input((">Introduce los apellidos del contacto: ")))
        nuevocontacto.SetFechaNacimiento(input((">Introduce la fecha de nacimiento del contacto: ")))

        telefonos = []
        fin = ""
        while fin != "No":
            fin = input(">¿Quieres añadir un teléfono? Si / No:")
            if fin == "Si":    
                nuevotelefono = Telefono.Telefono()
                nuevotelefono.SetNumeroTelefono(input((">Introduce el telefono del contacto: ")))
                nuevotelefono.SetDescripcion(input((">Introduce la descripción del telefono: ")))
        
                telefonos.append(nuevotelefono)
        nuevocontacto.SetListaTelefonos(telefonos)

        direcciones = []
        fin = ""
        while fin != "No":
            fin = input(">¿Quieres añadir una direccion? Si / No:")
            if fin == "Si":    
                nuevadireccion = Direccion.Direccion()
                nuevadireccion.SetCalle(input((">Introduce la calle de la direccion del contacto: ")))
                nuevadireccion.SetPiso(input((">Introduce el piso de la direccion del contacto: ")))
                nuevadireccion.SetCiudad(input((">Introduce la ciudad del contacto: ")))
                nuevadireccion.SetCodigoPostal(input((">Introduce el codigo postal del contacto: ")))
                direcciones.append(nuevadireccion)
        nuevocontacto.SetListaDirecciones(direcciones)
        
        return Conversion.ContactoAString(nuevocontacto)
    except:
        print("ERROR: Proceso de crear un contacto")
        return None
