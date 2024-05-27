# Gestor de Contactos

Este proyecto es una aplicación cliente-servidor para gestionar contactos. Está dividido en dos partes: un servidor y un cliente. El servidor acepta múltiples conexiones de clientes simultáneamente gracias a la implementación con hilos. Los datos de los contactos se guardan en una base de datos SQLite3 que debe estar en el mismo directorio que los archivos del servidor.

## Características

- **Gestión de Contactos**: Permite crear, visualizar, y eliminar contactos.
- **Multicliente**: El servidor puede manejar múltiples conexiones de clientes al mismo tiempo utilizando hilos.
- **Base de Datos**: Utiliza SQLite3 para almacenar la información de los contactos. El archivo de la base de datos debe estar en el mismo directorio que los archivos del servidor.
- **Configuración por Defecto**: Tanto el servidor como el cliente están configurados para funcionar en la IP `127.0.0.1` y el puerto `30000`. Si se desea usar la aplicación a través de la red, es necesario cambiar estos valores en los archivos correspondientes.

## Estructura del Proyecto

- **Servidor**
  - `Servidor.py`: Archivo principal del servidor que maneja las conexiones de los clientes.
  - `BaseDatos.py`: Módulo para gestionar la base de datos SQLite3.
  - `Contacto.py`: Clase que define la estructura de un contacto.
  - `Telefono.py`: Clase que define la estructura de un teléfono asociado a un contacto.
  - `Direccion.py`: Clase que define la estructura de una dirección asociada a un contacto.
  - `Conversion.py`: Módulo que maneja la conversión entre objetos y cadenas de texto.

- **Cliente**
  - `Gestor_Contactos.py`: Archivo principal del cliente que se conecta al servidor.
  - `Contacto.py`: Clase que define la estructura de un contacto.
  - `Telefono.py`: Clase que define la estructura de un teléfono asociado a un contacto.
  - `Direccion.py`: Clase que define la estructura de una dirección asociada a un contacto.
  - `Visualizacion.py`: Módulo que maneja la interfaz de usuario en la línea de comandos.
  - `Conversion.py`: Módulo que maneja la conversión entre objetos y cadenas de texto.

## Configuración

### Servidor

1. Asegúrate de que el archivo de la base de datos `Contactos.db` está en el mismo directorio que `Servidor.py`.
2. Ejecuta el servidor con el comando:
   ```sh
   python Servidor.py
   ```

### Cliente

1. Configura la IP y el puerto en `Gestor_Contactos.py` si es necesario.
2. Ejecuta el cliente con el comando:
   ```sh
   python Gestor_Contactos.py
   ```

## Uso

### Menú Principal del Cliente

1. **Ver Contacto**: Permite buscar y visualizar contactos.
2. **Crear Contacto Nuevo**: Permite crear un nuevo contacto.
3. **Borrar Contacto**: Permite borrar contactos.
4. **Mostrar Todos los Contactos**: Muestra todos los contactos guardados.
5. **Salir**: Cierra la conexión con el servidor y termina la aplicación.

### Notas

- Para cambiar la IP y el puerto, modifica las siguientes líneas en `Gestor_Contactos.py` (cliente) y `Servidor.py`:
  ```python
  host = '127.0.0.1'
  puerto = 30000
  ```

## Requisitos

- Python 3.x
- SQLite3

## Instalación

1. Clona el repositorio:
   ```sh
   git clone https://github.com/tu_usuario/gestor_contactos.git
   ```
2. Navega al directorio del proyecto:
   ```sh
   cd gestor_contactos
   ```
3. Asegúrate de que tienes Python y SQLite3 instalados en tu sistema.

---
