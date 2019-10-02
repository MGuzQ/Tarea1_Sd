import socket 
import os


def main():
#ip del container servidor(server) 
	#host = input('\nIngrese la ip del servidor :')

	port = 5000

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

	s.connect(("10.5.0.5",port)) 
#mensaje de "handshake"
	message = "Hola servidor"
	s.send(message.encode('ascii'))
	i=1
	if not os.path.exists("../respuestas"):
		os.makedirs("../respuestas")
	arch = open("../respuestas/respuestas.txt", 'a')
	while True: 
		 
#mensaje del servidor
		data = s.recv(1024) 
		print('Servidor :',str(data.decode('ascii')))
		arch.write(str(data.decode('ascii')) + "\n")
#mensaje a enviar (lo dice el print del input >:[ )
		
		ans = "Mensaje "+str(i)
		if i == 10: 
			break
		else:
			#enviar el mensaje en ascii
			i = i + 1
			s.send(ans.encode('ascii'))
			continue
	arch.close()
	s.close() 

main() 
