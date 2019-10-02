FROM ubuntu:latest

RUN apt-get update \
	&& apt-get -y install python3 \
	&& apt-get -y install python3-pip \
	&& apt-get -y install iproute2 \
	&& apt-get -y install nano


CMD ["mkdir","Data2"]
COPY datanode2.py /Data2/datanode2.py
CMD ["python3", "-u", "Data2/datanode2.py"]

