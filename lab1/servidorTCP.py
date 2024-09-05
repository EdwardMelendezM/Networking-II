# ServidorTCP.py
from socket import *
# inicializar variables
puertoServidor = 65432
# crear socket de escucha (o de bienvenida)
socketServidor = socket(AF_INET,SOCK_STREAM)
# asociar nro. puerto del servidor con el socket
socketServidor.bind(('',puertoServidor))
# servidor se queda escuchando por peticiones de conexión TCP
# (desde el cliente, con un máximo de conexiones en cola de 2)
socketServidor.listen(2)
print ('El servidor está listo para escuchar')
# lazo 'eterno'
while True:
  # el servidor espera en el metodo accept() por peticiones entrantes,
  # un nuevo socket dedicado para este cliene en particular es
  # creado al retorno de este metodo
  socketConexion, addr = socketServidor.accept()
  # leer solo los bytes desde el socket
  sentencia = socketConexion.recv(1024).decode()
  # capitalizar la sentencia
  sentenciaCapitalizada = sentencia.upper()
  # enviar sentencia modificada de regreso al cliente
  socketConexion.send(sentenciaCapitalizada.encode())
  # cerrar la conexión a este cliente (el socket de escucha sigue abierto)
  socketConexion.close()

  # Watch services of port 65432
  # netstat -an | findstr :65432