import socket
import threading
import Comunicacion

SocketServidor = socket.socket()
host = '127.0.0.1'
puerto = 30000
SocketServidor.bind((host, puerto))

SocketServidor.listen()

print(f"Servidor iniciado!\nhost: {host}\nPuerto: {puerto}")

while True:
    cliente, direccion = SocketServidor.accept()
    print('Nuevo cliente conectado: ' + direccion[0] + ':' + str(direccion[1]))
    hilo = threading.Thread(target=Comunicacion.HiloCliente,args=(cliente,direccion[0] + ':' + str(direccion[1]),))
    hilo.start()
SocketServidor.close()
