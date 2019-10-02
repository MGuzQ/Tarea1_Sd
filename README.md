# Tarea1_Sdg

Integrantes:
- Matías Guzmán 201673588-7
- Victoria Miranda 201604521-k

Tarea 1 de Sistemas de gestion, arquitectura cliente servidor usando dockers y arquitectura tipo hadoop con 3 nodos

Para ejecutar esta aplicacion se requiere docker y se necesitan usar los comandos docker-compose build para la construccion de los containers y docker-compose up para el levantamiento automatico de estos. Al finalizar la ejecucion, usar el comando docker-compose down para liberar la red estatica que se definio con tal de no causar problemas.

Se debe tener en consideracion que usamos una red estatica para la conexion entre las partes, por lo que en caso de que se tengan otros servicios levantados podria haber colision.

La ruta de los archivos "log" para cliente-servidor son:
* Cliente-Servidor/cliente/respuestas/respuestas.txt Para las respuestas recibidas por el cliente
* Cliente-Servidor/servidor/logs/log.txt Para el registro de mensajes que envia el cliente

La ruta de los archivos "log" para la arquitectura hadoop son:
* Hadoop/client/logs/registro_cliente.txt   Indica que mensaje se guardo en que nodo
* Hadoop/datanode1/logs/data.txt    Indica los mensajes que recibio del cliente(por el headnode)
* Hadoop/datanode2/logs/data.txt    Indica los mensajes que recibio del cliente(por el headnode)
* Hadoop/datanode3/logs/data.txt    Indica los mensajes que recibio del cliente(por el headnode)
* Hadoop/headnode/logs/hearbeat_server.txt  Indica cada 5s que headnodes estan en ejecucion
* Hadoop/headnode/logs/registro_server.txt  Indica que datanode tiene los mensajes del cliente
