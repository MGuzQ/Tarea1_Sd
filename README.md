# Tarea1_Sdg

Integrantes:
- Matías Guzmán 201673588-7
- Victoria Miranda 201604521-k

Tarea 1 de Sistemas Distribuidos, arquitectura cliente servidor usando dockers y arquitectura tipo hadoop con 3 nodos

Para ejecutar esta aplicación se requiere docker y se necesitan usar los comandos docker-compose build para la construcción de los containers y docker-compose up para el levantamiento automático de estos. Al finalizar la ejecución, usar el comando docker-compose down para liberar la red estática que se definió con tal de no causar problemas.

Se debe tener en consideración que usamos una red estática para la conexión entre las partes, por lo que en caso de que se tengan otros servicios levantados podria haber colisión.

La ruta de los archivos "log" para cliente-servidor son:
* Cliente-Servidor/cliente/respuestas/respuestas.txt Para las respuestas recibidas por el cliente
* Cliente-Servidor/servidor/logs/log.txt Para el registro de mensajes que envía el cliente

La ruta de los archivos "log" para la arquitectura hadoop son:
* Hadoop/client/logs/registro_cliente.txt   Indica que mensaje se guardo en que nodo
* Hadoop/datanode1/logs/data.txt    Indica los mensajes que recibió del cliente(por el headnode)
* Hadoop/datanode2/logs/data.txt    Indica los mensajes que recibió del cliente(por el headnode)
* Hadoop/datanode3/logs/data.txt    Indica los mensajes que recibió del cliente(por el headnode)
* Hadoop/headnode/logs/hearbeat_server.txt  Indica cada 5s que headnodes estan en ejecucion
<<<<<<< HEAD
* Hadoop/headnode/logs/registro_server.txt  Indica qué datanode tiene los mensajes del cliente
=======
* Hadoop/headnode/logs/registro_server.txt  Indica qué datanode tiene los mensajes del cliente
>>>>>>> 05728c7a1fe6aa29f045e33060dbe33bf679e9b3
