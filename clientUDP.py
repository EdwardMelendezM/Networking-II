# ClienteUDP.py
from socket import *

# Inicializar variables
idServidor = '127.0.0.1'  # Reemplazar con la dirección IP real del servidor o 'localhost' si está en la misma máquina
puertoServidor = 12000

# Crear socket cliente UDP
socketCliente = socket(AF_INET, SOCK_DGRAM)

# Obtener alguna entrada desde el teclado del usuario
mensaje = input('Entrar una sentencia en minúsculas: ')

# Adjuntar nombre del servidor y el puerto al mensaje
# y enviarlo hacia el socket
socketCliente.sendto(mensaje.encode(), (idServidor, puertoServidor))

# Leer caracteres replicados que llegaron al socket hacia un string
mensajeModificado, direccionServidor = socketCliente.recvfrom(2048)

# Imprimir string recibido
print(mensajeModificado.decode())

# Cerrar socket
socketCliente.close()