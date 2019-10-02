import socket 
from _thread import *
import threading
import time
import random
import struct
import sys
import os
from random import randrange

def broadcastThread(dummy,c):
    if not os.path.exists("../logs"):
        os.makedirs("../logs")
    
    registro_hb = open("../logs/hearbeat_server.txt", "a")
    while True:
        print("bump bump")
        sent = c.sendto(b'Estas vivo?', ('224.3.29.71', 5001))
        while True:
            print('Esperando respuestas')
            try:
                data, server = c.recvfrom(16)
            except socket.timeout:
                break
            else:
                print('se recibio {!r} de {}'.format(data, server))
                registro_hb.write(str(server[0])+" esta up \n")

        time.sleep(5)
        registro_hb.write("5s HearBeat \n")
    registro_hb.write("Fin \n")
    registro_hb.close()

hnHost = ''
#puertos de comunicacion con cliente y datanodes
cPort = 5000
dn1Port = 5002
dn2Port = 5003
dn3Port = 5004


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #socket con cliente

dn1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
dn2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #sockets con datanodes para envio de mensajes
dn3 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Configuraciones pra el multicast
dn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #socket para multicast
dn.settimeout(5)
ttl = struct.pack('b', 1)
dn.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)


s.bind((hnHost,cPort))

dn1.bind((hnHost,dn1Port))
dn2.bind((hnHost,dn2Port))
dn3.bind((hnHost,dn3Port))

s.listen()
dn1.listen()
dn2.listen()
dn3.listen()



#envia broadcast
start_new_thread(broadcastThread,(0,dn))

#se conecta con cliente y datanodes 
conn, addr = s.accept()
conn1, addr1 = dn1.accept()
conn2, addr2 = dn2.accept()
conn3, addr3 = dn3.accept()
print("Conectado con "+str(addr[0])+" en puerto "+str(addr[1]))

if not os.path.exists("../logs"):
    os.makedirs("../logs")
registro = open("../logs/registro_server.txt", "w")
i = 0
while True:
    data = ""
    data = conn.recv(1024)
    if not data:
        conn.close()
        conn1.sendall(b'exit')
        conn2.sendall(b'exit')
        conn3.sendall(b'exit')
        sent = dn.sendto(b'exit', ('224.3.29.71', 5001))
        break
    #conn.sendall(b"me llego tu mensaje")
    index = randrange(3)
    lista = [conn1,conn2,conn3]
    lista[index].sendall(data)
    i+=1
    respuesta = "me llego tu mensaje y se guardo en datanode "+str(index+1)
    registro.write("datanode "+str(index+1)+" tiene el mensaje: "+data.decode('ascii')+str("\n"))
    conn.sendall(respuesta.encode('ascii'))
registro.close()
