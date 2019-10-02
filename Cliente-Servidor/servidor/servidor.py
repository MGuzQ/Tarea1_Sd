import socket 
from _thread import *
import threading 
import os

print_lock = threading.Lock() 
#threadpool para recibir mas de un cliente
def threaded(c):
	if not os.path.exists("../logs"):
		os.makedirs("../logs")
	arch = open("../logs/log.txt",'a') 
	while True: 
		#mensaje recibido por el servidor
		data = c.recv(1024) 
		#cuando el cliente se desconecta
		if not data: 
			print('No se recibio data') 
			print_lock.release() 
			break
		#cuando el cliente envia un mensaje
		print("Cliente: ",str(data.decode('ascii')))
		arch.write(str(data.decode('ascii')) + "\n")
		mensaje = "Se recibio tu mensaje "+ str(data.decode('ascii'))
		c.send(mensaje.encode('ascii')) 
	arch.close()
	c.close() 


def main():
	#definir la conexion 
	#host = "" 
	port = 5000
	#declarar el socket y el tipo (TCP, llegan ordenados :])
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	#darle ip y puerto al socket
	s.bind(("", port)) 
	print("El socket esta en el puerto", port) 
	#maximo de clientes (5)
	s.listen(5) 
	print("Esperando conexiones") 

	while True: 
		#aceptar un cliente
		c, addr = s.accept() 
		#cliente toma la hebra
		print_lock.acquire() 
		print('Conexion en :', addr[0], ':', addr[1]) 

		start_new_thread(threaded, (c,)) 
	#matamos la conexion
	s.close() 


main() 
