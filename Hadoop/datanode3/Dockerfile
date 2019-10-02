FROM ubuntu:latest

RUN apt-get update \
	&& apt-get -y install python3 \
	&& apt-get -y install python3-pip \
	&& apt-get -y install iproute2 \
	&& apt-get -y install nano


CMD ["mkdir","Data3"]
COPY datanode3.py /Data3/datanode3.py
CMD ["python3", "-u", "Data3/datanode3.py"]

