# ServidorUDP.py
from socket import *
# inicializar variables
puertoServidor = 12000
# crear socket servidor UDP
socketServidor = socket(AF_INET, SOCK_DGRAM)
# enlazar socket al nro. de puerto local 12000
socketServidor.bind(('', puertoServidor))
# mensaje: que el servidor está listo
print('El servidor está listo para recibir')
# lazo 'eterno'
while True:
  # leer desde el socket UDP para cargar el mensaje,

  # y obtener la dirección del cliente (el IP y el nro. puerto del cliente)
  mensaje, direccionCliente = socketServidor.recvfrom(2048)
  # cambiar mensaje a mayúsculas
  print('Mensaje:', mensaje.decode())
  mensajeModificado = mensaje.decode().upper()
  # enviar mensaje modificado de regreso al cliente
  socketServidor.sendto(mensajeModificado.encode(), direccionCliente)