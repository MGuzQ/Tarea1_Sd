FROM ubuntu:latest

RUN apt-get update \
	&& apt-get -y install python3 \
	&& apt-get -y install python3-pip \
	&& apt-get -y install iproute2 \
	&& apt-get -y install nano


CMD ["mkdir","client"]
COPY cliente.py /client/cliente.py
CMD ["python3", "-u", "client/cliente.py"]
