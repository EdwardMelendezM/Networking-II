# ClienteTCP.py
from socket import *
# inicializar variables
idServidor = '127.0.0.1'
#idServidor = '192.168.1.36'
puertoServidor = 65432
# crear socket TCP para comunicarse con el servidor,
# en el puerto remoto 65432
socketCliente = socket(AF_INET, SOCK_STREAM)
# iniciar conexión TCP hacia el servidor, indicando la dirección del servidor
socketCliente.connect((idServidor, puertoServidor))
# obtener alguna entrada desde el teclado del usuario
mensaje = input('Entrar una sentencia en minúsculas:')

# enviar el string a traves del socket del cliente hacia la conexión TCP
socketCliente.send(mensaje.encode())
# ¡el cliente se queda en espera!
# leer desde su socket, los datos son colocados en el string mensajeModificado
mensajeModificado = socketCliente.recv(1024)
# imprimir string recibido
print ('Desde el servidor:', mensajeModificado.decode())
# cerrar socket
socketCliente.close()