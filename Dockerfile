FROM mur2/pandoc:1.0.11

ARG DEBIAN_FRONTEND=noninteractive

# the user which run the application
RUN useradd -s /bin/bash mur2
# user home dir
WORKDIR /home/mur2

# update the packages
RUN apt-get update -y

# update nodehs and npm
RUN apt-get update -y && apt-get install -y git gnupg2  curl dirmngr apt-transport-https lsb-release ca-certificates unzip make g++ software-properties-common
RUN ( curl -sL https://deb.nodesource.com/setup_12.x | bash - ) && apt -y install nodejs && npm update npm -g  && node --version && npm --version

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
WORKDIR /home/mur2/npm
RUN su mur2 -c "npm install" -

# start the application
ENV FLASK_APP mur2.py
CMD su mur2 -c "/bin/bash /home/mur2/boot.sh" -
