FROM mur2/iupmath:1.0.3

ARG DEBIAN_FRONTEND=noninteractive

# user home dir
WORKDIR /home/mur2

# update the packages
RUN apt-get update -y

# install the necesarry python packages
COPY requirements.txt requirements.txt
RUN pip install -U pip setuptools
RUN pip install -r requirements.txt
# install jwt for confluence this is conflict with the PyJWT so we do from git
WORKDIR /tmp
RUN git clone https://github.com/sajozsattila/python-jwt && cd python-jwt && pip install .
WORKDIR /home/mur2

# install the application
COPY app ./app
COPY npm ./npm
RUN mkdir user_data
COPY app.db ./
COPY waitress_server.sh boot.sh ./
RUN chmod +x waitress_server.sh
COPY config.py ./config.py
RUN mkdir /home/mur2/logs && chown mur2 /home/mur2/logs && chgrp mur2 /home/mur2/logs
RUN chown -R mur2:mur2 ./

# start the application
ENV FLASK_APP mur2.py
CMD su mur2 -c "/bin/bash /home/mur2/boot.sh" -
