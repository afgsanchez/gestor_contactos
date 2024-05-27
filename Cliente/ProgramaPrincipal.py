import socket
import Contacto
import Telefono
import Direccion
import Visualizacion

SocketCliente = socket.socket()
host = '127.0.0.1'
puerto = 30000
SocketCliente.connect((host, puerto))
print('¡Conectado al servidor!')

while True:
    Visualizacion.MostrarMenu()
    opcion = Visualizacion.ObtenerOpcion('Opcion: ')
    # Buscar contactos (Visualizar)
    if opcion == 1:        
        Visualizacion.MostrarMenuBuscar()
        finbuscar = False
        while not finbuscar:
            opcionbuscar = Visualizacion.ObtenerOpcion('Opcion: ')
            if opcionbuscar == 1:
                parametro = input("Introduzca el nombre: ")
                finbuscar = True
            elif opcionbuscar == 2:
                finbuscar = True
                parametro = input("Introduzca el teléfono: ")
            elif opcionbuscar == 3:
                finbuscar = True
        if opcionbuscar != 3:
            try:
                mensaje = str(opcion) + "&" + str(opcionbuscar) + "&" + parametro
                SocketCliente.send(str.encode(mensaje))
                recibido = SocketCliente.recv(4096)
                recibido = recibido.decode('utf-8')
                print(recibido)
                Visualizacion.MostrarContactos(recibido)
            except Exception as e:
                print("ERROR: Búsqueda de contactos.", e)
    # Crear contacto nuevo
    elif opcion == 2:
        try:
            nuevocontacto = Visualizacion.ProcesoCrearContacto()
            SocketCliente.send(str.encode(str(opcion) + "&" + nuevocontacto))
            recibido = SocketCliente.recv(4096)
            recibido = recibido.decode('utf-8')
            if recibido == "1":
                print("# Contacto insertado")
            else:
                print("ERROR: No se puede insertar el contacto")
        except Exception as e:
            print("ERROR: Creando un contacto.", e)
    # Borrar contactos
    elif opcion == 3:
        Visualizacion.MostrarMenuBorrar()
        finbuscar = False
        while not finbuscar:
            opcionbuscar = Visualizacion.ObtenerOpcion('Opcion: ')
            if opcionbuscar == 1:
                parametro = input("Introduzca el nombre: ")
                finbuscar = True
            elif opcionbuscar == 2:
                finbuscar = True
                parametro = input("Introduzca el teléfono: ")
            elif opcionbuscar == 3:
                finbuscar = True
        if opcionbuscar != 3:
            try:
                mensaje = str(opcion) + "&" + str(opcionbuscar) + "&" + parametro
                SocketCliente.send(str.encode(mensaje))
                recibido = SocketCliente.recv(4096)
                recibido = recibido.decode('utf-8')
                if recibido == "1":
                    print("# Contactos borrados")
                else:
                    print("ERROR: Se produjeron errores durante el borrado")
            except Exception as e:
                print("ERROR: Borrando contactos.", e)
    # Mostrar todos los contactos
    elif opcion == 4:
        try:            
            SocketCliente.send(str.encode(str(opcion)))
            recibido = SocketCliente.recv(4096)
            recibido = recibido.decode('utf-8')
            Visualizacion.MostrarContactos(recibido)
        except Exception as e:
            print("ERROR: Mostrando todos los contactos.", e)
    # Salir
    elif opcion == 5:
        SocketCliente.send(str.encode(str(opcion)))
        print("Cerrando cliente...")
        break

SocketCliente.close()
