import socket
import os
import time
dnHost = '10.5.0.2'
dnPort = 5000
if not os.path.exists("../logs"):
	os.makedirs("../logs")
registro = open("../logs/registro_cliente.txt", "w")
#se conecta al servidor
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((dnHost,dnPort))
cont=1
while True:
	#msje = input("Envie un mensaje al headnode o escriba exit para salir\n")
	msje = "Mensaje " + str(cont)
	
	if (cont == 10):
		msje = "exit"
	if (msje == "exit"):
	   break
	s.sendall(msje.encode('ascii'))
	data = s.recv(1024)
	print("server: "+data.decode('ascii'))
	node = data.decode('ascii')[-1]
	registro.write("Mensaje "+msje+" guardado en datanode "+str(node)+str("\n"))
	cont = cont + 1
	time.sleep(2)
registro.write("Fin \n")
registro.close()
