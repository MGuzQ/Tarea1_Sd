import socket
import struct
import sys
from _thread import *
import os

#node 1
multicast_group = '224.3.29.71'
server_address = ('', 5001)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(server_address)
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_ADD_MEMBERSHIP,
    mreq)



hnHost = '10.5.0.2'
hnPort = 5002

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((hnHost,hnPort))

def M_cliente(dummy,c):
    if not os.path.exists("../logs"):
        os.makedirs("../logs")
    data = open("../logs/data.txt", "a")
    while True:
        re = c.recv(1024)
        if (re == b"exit"):
            print("entro")
            break
        cliente = re.decode('ascii')+str("\n")
        data.write(str(cliente))
    data.write("Fin \n")
    data.close()

start_new_thread(M_cliente,(0,s))

while True:
    print('\nEsperando mensaje')
    data, address = sock.recvfrom(1024)

    print('Se recibieron {} bytes de {}'.format(
        len(data), address))
    print(data)
    if (data == b'exit' ):
    	break
    print('Enviando signos de vida a ', address)
    sock.sendto(b'Estoy vivo', address)


    

    
    	
    	
    
    



