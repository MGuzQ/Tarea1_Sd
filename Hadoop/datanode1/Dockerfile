FROM ubuntu:latest

RUN apt-get update \
	&& apt-get -y install python3 \
	&& apt-get -y install python3-pip \
	&& apt-get -y install iproute2 \
	&& apt-get -y install nano


CMD ["mkdir","Data1"]
COPY datanode1.py /Data1/datanode1.py
CMD ["python3", "-u", "Data1/datanode1.py"]
