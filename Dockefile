# syntax=docker/dockerfile:1
FROM ubuntu
RUN apt update
RUN apt install apt-utils -y
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata
RUN apt install git -y
RUN apt install sudo -y
RUN apt install pip -y
WORKDIR /opt
RUN git clone https://github.com/tlh45342/flask-example2.git
WORKDIR /opt/flask-example2
RUN pip install -r requirements.txt
RUN bash install-services.sh
CMD python3 server.py
